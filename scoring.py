def player_pitching_score(player, error_list):
    # Check if the player is a pitcher
    if player.PlayerPosition != "Pitcher":
        return 0

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
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} is missing {attr}")

    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Calculate each component of the pitching score
    era_score = validate_and_standardize('PlayerERA', player, standardize_low, error_list) * 0.5
    whip_score = validate_and_standardize('PlayerWHIP', player, standardize_low, error_list) * 0.3
    ks_score = validate_and_standardize('PlayerKs', player, standardize_high, error_list, low=False, divisor='PlayerIP') * 0.11
    bb_score = validate_and_standardize('PlayerBB', player, standardize_low, error_list, divisor='PlayerIP') * 0.07
    baa_score = validate_and_standardize('PlayerBAA', player, standardize_low, error_list) * 0.02

    pitching_score = era_score + whip_score + baa_score + ks_score + bb_score
    return pitching_score


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
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} is missing {attr}")

    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Calculate each component of the catching score
    fielding_perc_score = validate_and_standardize('FieldingPerc', player, standardize_high, error_list) * 0.6
    sb_score = validate_and_standardize('PlayerSB', player, standardize_low, error_list, divisor='PlayerATT') * 0.25
    arm_velo_score = validate_and_standardize('PlayerArmVelo', player, standardize_high, error_list) * 0.1
    att_score = validate_and_standardize('PlayerATT', player, standardize_low, error_list) * 0.05

    catching_score = fielding_perc_score + arm_velo_score + sb_score + att_score
    return catching_score


def player_defense_score(player, error_list):
    # Check for all necessary attributes before proceeding
    required_attributes = ['FieldingPerc', 'TotalChances', 'Assist', 'Putouts']
    missing_attrs = [
        attr for attr in required_attributes
        if not hasattr(player, attr)
    ]
    
    # Append errors for missing attributes
    for attr in missing_attrs:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} is missing {attr}")

    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Calculate each component of the defensive score
    fielding_score = validate_and_standardize('FieldingPerc', player, standardize_high, error_list) * 0.76

    # For ratios involving TotalChances, handle potential division by zero
    tc_score = validate_and_standardize('TotalChances', player, standardize_high, error_list, divisor='FieldingPerc') * 0.2
    assists_score = validate_and_standardize('Assist', player, standardize_high, error_list, divisor='TotalChances') * 0.02
    po_score = validate_and_standardize('Putouts', player, standardize_high, error_list, divisor='TotalChances') * 0.02

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
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} is missing {attr}")
    
    # If any attributes are missing, return an error score or handle as needed
    if missing_attrs:
        return 0

    # Calculate each component of the batting score
    avg_score = validate_and_standardize('PlayerBA', player, standardize_high, error_list) * 0.3
    ops_score = validate_and_standardize('PlayerOPS', player, standardize_high, error_list) * 0.3
    obp_score = validate_and_standardize('PlayerOBP', player, standardize_high, error_list) * 0.3
    rbi_score = validate_and_standardize('PlayerRBI', player, standardize_high, error_list) * 0.08
    strikeouts_score = validate_and_standardize('PlayerStrikeOuts', player, standardize_low, error_list) * 0.01
    hits_score = validate_and_standardize('PlayerHits', player, standardize_high, error_list) * 0.01

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

def validate_and_standardize(attr_name, player, standardize_func, error_list, low=True, divisor=None):
    try:
        value = float(getattr(player, attr_name))
        if divisor:
            divisor_value = float(getattr(player, divisor))
            if divisor_value == 0:
                raise ZeroDivisionError
            value /= divisor_value
        return standardize_func(value) if low else standardize_func(value)
    except (ValueError, AttributeError, ZeroDivisionError):
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} has invalid {attr_name}: {getattr(player, attr_name)}")
        return 0
