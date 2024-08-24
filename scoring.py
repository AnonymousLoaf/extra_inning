def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0


def player_pitching_score(player, error_list):
    # Check if the player is a pitcher
    if player.PlayerPosition != "Pitcher":
        return 0  # Early return if not a pitcher

    # Check for all necessary attributes before proceeding
    required_attributes = [
        'PlayerERA', 'PlayerWHIP', 'PlayerBAA', 'PlayerKs', 'PlayerIP', 'PlayerBB'
    ]
    missing_attrs = [
        attr for attr in required_attributes
        if not hasattr(player, attr)
    ]
    
    # Append errors for missing attributes
    for attr in missing_attrs:
        error_list.append(f"Cannot rank {player.PlayerFirstName} {player.PlayerLastName} Invalid value in: {attr}")

    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Calculate each component of the pitching score safely
    try:
        era_score = standardize_low(float(player.PlayerERA)) * 0.5
        whip_score = standardize_low(float(player.PlayerWHIP)) * 0.3
        baa_score = standardize_low(float(player.PlayerBAA)) * 0.02
        ks_score = standardize_high(float(player.PlayerKs) / float(player.PlayerIP)) * 0.11
        bb_score = standardize_low(float(player.PlayerBB) / float(player.PlayerIP)) * 0.07
        pitching_score = era_score + whip_score + baa_score + ks_score + bb_score
        return pitching_score
    except ZeroDivisionError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} cannot divide by zero: Player IP: {player.PlayerIP}")
        return 0  # or an appropriate error value


def player_catching_score(player, error_list):
    # Check if the player is a catcher
    if player.PlayerPosition != "Catcher":
        return 0  # Early return if not a catcher

    # Check for all necessary attributes before proceeding
    required_attributes = [
        'FieldingPerc', 'PlayerSB', 'PlayerATT', 'PlayerArmVelo'
    ]
    missing_attrs = [
        attr for attr in required_attributes
        if not hasattr(player, attr)
    ]
    
    # Append errors for missing attributes
    for attr in missing_attrs:
        error_list.append(f"Cannot rank {player.PlayerFirstName} {player.PlayerLastName} Invalid value in: {attr}")

    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Calculate each component of the catching score
    try:
        fielding_perc_score = standardize_high(float(player.FieldingPerc)) * 0.6
        sb_score = standardize_low(float(player.PlayerSB) / float(player.PlayerATT)) * 0.25
        arm_velo_score = standardize_high(float(player.PlayerArmVelo)) * 0.1
        att_score = standardize_low(float(player.PlayerATT)) * 0.05
        catching_score = fielding_perc_score + arm_velo_score + sb_score + att_score
        return catching_score
    except ZeroDivisionError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} cannot divide by zero: Player ATT: {player.PlayerATT}")
        return 0  # or an appropriate error value


def player_defense_score(player, error_list):
    # Check for all necessary attributes before proceeding
    required_attributes = ['FieldingPerc', 'TotalChances', 'Assist', 'Putouts']
    missing_attrs = [
        attr for attr in required_attributes
        if not hasattr(player, attr)
    ]
    
    # Append errors for missing attributes
    for attr in missing_attrs:
        error_list.append(f"Cannot rank {player.PlayerFirstName} {player.PlayerLastName} Invalid value in: {attr}")

    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Convert all attributes to float
    try:
        fielding_perc = float(player.FieldingPerc)
    except ValueError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} has invalid Fielding Percentage: {player.FieldingPerc}")
        fielding_perc = 0
    try:
        total_chances = float(player.TotalChances)
    except ValueError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} has invalid Total Chances: {player.Total_Chances}")
        total_chances = 0
    try:
        assists = float(player.Assist)
    except ValueError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} has invalid Assists: {player.Assist}")
        assists = 0
    try:
        putouts = float(player.Putouts)
    except ValueError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} has invalid Putouts: {player.Putouts}")
        putouts = 0

    # Calculate each component of the defensive score
    fielding_score = standardize_high(fielding_perc) * 0.76
    try:
        tc_score = standardize_high(total_chances / fielding_perc) * 0.2
    except ZeroDivisionError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} cannot divide by zero: Fielding Percentage: {fielding_perc}")
        tc_score = 0  # or an appropriate error value

    try:
        assists_score = standardize_high(assists / total_chances) * 0.02
    except ZeroDivisionError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} cannot divide by zero: Player Total Chances: {total_chances}")
        assists_score = 0  # or an appropriate error value

    try:
        po_score = standardize_high(putouts / total_chances) * 0.02
    except ZeroDivisionError:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} cannot divide by zero: Player Total Chances: {total_chances}")
        po_score = 0  # or an appropriate error value

    # Calculate the total defensive score
    defense_score = fielding_score + tc_score + assists_score + po_score
    
    return defense_score


def player_batting_score(player, error_list):
    # Check for all necessary attributes before proceeding
    required_attributes = [
        'PlayerBA', 'PlayerOPS', 'PlayerOBP', 'PlayerRBI', 'PlayerStrikeOuts', 'PlayerHits'
    ]
    missing_attrs = [
        attr for attr in required_attributes
        if not hasattr(player, attr)
    ]
    
    # Append errors for missing attributes
    for attr in missing_attrs:
        error_list.append(f"Cannot rank {player.PlayerFirstName} {player.PlayerLastName} Invalid value in: {attr}")
    
    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Calculate each component of the batting score
    avg_score = standardize_high(float(player.PlayerBA)) * 0.3
    ops_score = standardize_high(float(player.PlayerOPS)) * 0.3
    obp_score = standardize_high(float(player.PlayerOBP)) * 0.3
    rbi_score = standardize_high(float(player.PlayerRBI)) * 0.08
    strikeouts_score = standardize_low(float(player.PlayerStrikeOuts)) * 0.01
    hits_score = standardize_high(float(player.PlayerHits)) * 0.01

    # Calculate the total batting score
    batting_score = avg_score + ops_score + obp_score + rbi_score + strikeouts_score + hits_score
    
    return batting_score



def standardize_low(stat):
    if stat == 0:
        return 0
    elif stat <= 1:
        return stat
    return 1000 / (stat + 1000)


def standardize_high(stat):
    if stat == 0:
        return 0
    elif stat <= 1:
        return stat
    return 1000 / (1100 - stat)
