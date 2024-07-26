def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0


def player_defense_score(player):
    Fielding_Score = player.PlayerFieldingPercentage * 1
    TC_Score = player.PlayerTC * 0.95
    Assists_Score = player.PlayerAssists * 0.9
    PO_Score = player.PlayerPO * 0.85
    total_score = Fielding_Score + TC_Score + Assists_Score + PO_Score
    return total_score


def player_pitching_score(player):
    ERA_Score = player.PlayerERA * 1
    WHIP_Score = player.PlayerWHIP * 0.95
    BAA_Score = player.PlayerBAA * 0.9
    Ks_Score = player.PlayerKs * 0.85
    IP_Score = player.PlayerIP * 0.8
    BB_Score = player.PlayerBB * 0.75
    total_score = ERA_Score + WHIP_Score + BAA_Score + Ks_Score + IP_Score + BB_Score
    return total_score
    


def player_catching_score(player):
    SB_ATT_Score = player.PlayerSBATT * 1
    PopTime_Score = player.PlayerPopTime * 0.95
    ArmVelo_Score = player.PlayerArmVelo * 0.9
    total_score = SB_ATT_Score + PopTime_Score + ArmVelo_Score
    return total_score

def player_batting_score(player):
    AVG_Score = player.PlayerBA * 1
    OPS_Score = player.PlayerOPS * 0.95
    OBP_Score = player.PlayerOBP * 0.9
    AtBats_Score = player.PlayerAtBats * 0.85
    StrikeOuts_Score = player.PlayerStrikeOuts * 0.8
    Hits_Score = player.PlayerHits * 0.75