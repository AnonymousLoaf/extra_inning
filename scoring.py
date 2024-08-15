def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0


def player_pitching_score(player):
    era_score = standardize_low(player.PlayerERA) * 0.5
    whip_score = standardize_low(player.PlayerWHIP) * 0.3
    baa_score = standardize_low(player.PlayerBAA) * 0.02
    ks_score = standardize_high(player.PlayerKs / player.PlayerIP) * 0.11
    bb_score = standardize_low(player.PlayerBB / player.PlayerIP) * 0.07
    pitching_score = era_score + whip_score + baa_score + ks_score + bb_score
    return pitching_score


def player_catching_score(player):
    FieldingPerc_Score = standardize_high(player.FieldingPerc) * 0.5
    SB_Score = standardize_low(player.PlayerSB/player.PlayerATT) * 0.25
    PopTime_Score = standardize_low(player.PlayerPopTime) * 0.1
    ArmVelo_Score = standardize_high(player.PlayerArmVelo) * 0.1
    Att_Score = standardize_low(player.PlayerATT) * 0.05
    catching_score = FieldingPerc_Score + PopTime_Score + ArmVelo_Score + SB_Score + Att_Score
    return catching_score


def player_defense_score(player):
    fielding_score = standardize_high(player.FieldingPerc) * 0.62
    tc_score = standardize_high(player.TotalChances/player.FieldingPerc) * 0.34
    assists_score = standardize_high(player.Assist/player.TotalChances) * 0.02
    po_score = standardize_high(player.Putouts/player.TotalChances) * 0.02
    defense_score = fielding_score + tc_score + assists_score + po_score
    return defense_score


def player_batting_score(player):
    avg_score = standardize_high(player.PlayerBA) * 0.40
    ops_score = standardize_high(player.PlayerOPS) * 0.40
    obp_score = standardize_high(player.PlayerOBP) * 0.10
    rbi_score = standardize_high(player.PlayerRBI) * 0.08
    strikeouts_score = standardize_low(player.PlayerStrikeOuts) * 0.01
    hits_score = standardize_high(player.PlayerHits) * 0.01
    
    batting_score = avg_score + ops_score + obp_score + strikeouts_score + hits_score + rbi_score
    return batting_score


def standardize_low(stat):
    return 1000 / (stat + 1000)


def standardize_high(stat):
    return 1000 / (1100 - stat)
