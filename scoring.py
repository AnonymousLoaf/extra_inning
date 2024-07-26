def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0


def player_defense_score(player):
    fielding_score = player.FieldingPerc * 1
    tc_score = player.TotalChances * 0.95
    assists_score = player.Assist * 0.9
    po_score = player.Putouts * 0.85
    total_score = fielding_score + tc_score + assists_score + po_score
    return total_score


def player_pitching_score(player):
    era_score = player.PlayerERA * 1
    whip_score = player.PlayerWHIP * 0.95
    baa_score = player.PlayerBAA * 0.9
    ks_score = player.PlayerKs * 0.85
    ip_score = player.PlayerIP * 0.8
    bb_score = player.PlayerBB * 0.75
    total_score = era_score + whip_score + baa_score + ks_score + ip_score + bb_score
    return total_score

def player_catching_score(player):
    #SB_ATT_Score = player.PlayerSBATT * 1
    PopTime_Score = player.PlayerPopTime * 0.95
    ArmVelo_Score = player.PlayerArmVelo * 0.9
    total_score = PopTime_Score + ArmVelo_Score #+ SB_ATT_Score 
    return total_score


def player_batting_score(player):
    avg_score = player.PlayerBA * 1
    ops_score = player.PlayerOPS * 0.95
    obp_score = player.PlayerOBP * 0.9
    # atbats_score = player.PlayerAtBats * 0.85
    # strikeouts_score = player.PlayerStrikeOuts * 0.8
    # hits_score = player.PlayerHits * 0.75
    total_score = avg_score + ops_score + obp_score  # + atbats_score + strikeouts_score + hits_score
    return total_score
