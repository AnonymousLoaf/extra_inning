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
    sb_score = validate_and_standardize('PlayerSB', player, standardize_low, error_list, divisor='PlayerATT') * 0.30
    att_score = validate_and_standardize('PlayerATT', player, standardize_low, error_list) * 0.10

    catching_score = fielding_perc_score + sb_score + att_score
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
    fielding_score = validate_and_standardize('FieldingPerc', player, standardize_high, error_list) * 0.75

    # For ratios involving TotalChances, handle potential division by zero
    tc_score = validate_and_standardize('TotalChances', player, standardize_high, error_list, divisor='FieldingPerc') * 0.25

    # Calculate the total defensive score
    defense_score = fielding_score + tc_score
    
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
    avg_score = validate_and_standardize('PlayerBA', player, standardize_high, error_list) * 0.35
    ops_score = validate_and_standardize('PlayerOPS', player, standardize_high, error_list) * 0.25
    obp_score = validate_and_standardize('PlayerOBP', player, standardize_high, error_list) * 0.2
    rbi_score = validate_and_standardize('PlayerRBI', player, standardize_high, error_list) * 0.17
    strikeouts_score = validate_and_standardize('PlayerStrikeOuts', player, standardize_low, error_list) * 0.02
    hits_score = validate_and_standardize('PlayerHits', player, standardize_high, error_list) * 0.01

    # Calculate the total batting score
    batting_score = avg_score + ops_score + obp_score + rbi_score + strikeouts_score + hits_score
    
    return batting_score

def calculate_batting_rank(players, error_list, position_specific=False):
    # Step 1: Calculate batting score for each player and store in a list of tuples (player, score)
    player_scores = [
        (player, player_batting_score(player, error_list))
        for player in players
    ]

    # Step 2: Filter out players who have a batting score of 0 (optional)
    player_scores = [(player, score) for player, score in player_scores if score > 0]

    # Step 3: Sort players based on their batting score in descending order
    player_scores.sort(key=lambda x: x[1], reverse=True)

    if position_specific:
        # Step 4: Group players by their positions and rank within their positions
        position_ranks = {}
        for player, score in player_scores:
            position = player.PlayerPosition
            if position not in position_ranks:
                position_ranks[position] = []
            position_ranks[position].append((player, score))

        # Step 5: Assign rankings to each player within their position group
        for position, ranked_players in position_ranks.items():
            for rank, (player, score) in enumerate(ranked_players, start=1):
                player.pos_batting_rank = rank  # Update player's position batting rank
        return position_ranks
    
    else:
        # Step 4: Assign global rankings (all players)
        for rank, (player, score) in enumerate(player_scores, start=1):
            player.global_batting_rank = rank  # Update player's global batting rank
        return player_scores

def player_num_national_tournaments(player, error_list):
    # Check for all necessary attributes before proceeding
    required_attributes = ['TopTournaments']
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

    # Check if TopTournaments is a string and not empty or a float
    if not isinstance(player.TopTournaments, str):
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} has an invalid TopTournaments value")
        return 0

    natnl_tournaments = ["Atlanta Legacy", "Patriot Games", "PGF Show me the Money", "TFL Summer Championship", "Alliance Super Cup", "Colorado Sparkler",
                         "Dons Battle On", "Hotshots Summer Exposure", "IDT Boulder Colorado", "PGF Nationals", "Scenic City", "TC 7 inning series/Brashear summer invitational",
                         "TC Zoom into June", "TCS Nationals", "TCS P5 Showcase", "Top Gun Invitational", "Top Club National Championships", "Alliance National Championship"]
    
    # Convert player's TopTournaments into a lowercased list of tournaments for easier comparison
    player_tournaments = [tournament.strip().lower() for tournament in player.TopTournaments.split(',')]
    
    # Count how many national tournaments the player has participated in
    num_national_tournaments = sum(
        1 for tournament in natnl_tournaments if tournament.lower() in " ".join(player_tournaments)
    )

    return num_national_tournaments

def standardize_low(stat):
    if stat == 0:
        return 0
    return 1 / (1 + stat)


def standardize_high(stat):
    return stat / (1 + stat)

def validate_and_standardize(attr_name, player, standardize_func, error_list, low=True, divisor=None):
    try:
        value = float(getattr(player, attr_name))
        if divisor:
            divisor_value = float(getattr(player, divisor))
            # Skip division if divisor is zero, possibly log or handle it appropriately
            if divisor_value == 0:
                error_list.append(f"Warning: {player.PlayerFirstName} {player.PlayerLastName} in {player.PlayerPosition}: {divisor} is zero")
                return 0
            value /= divisor_value
        return standardize_func(value) if low else standardize_func(value)
    except (ValueError, AttributeError) as e:
        error_list.append(f"{player.PlayerFirstName} {player.PlayerLastName} has invalid {attr_name}: {getattr(player, attr_name, 'Unknown')}")
        return 0
