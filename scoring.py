def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0


def players_defensive_score(players):
    stats_to_check = [
        "FieldingPerc",
        "TotalChances",
        "Assist",
        "Putouts",
        "ArmVelo"]
    return sorted(players, key=lambda x: tuple(safe_float(getattr(x, stat)) for stat in stats_to_check), reverse=True)


def players_pitcher_score(players):
    stats_to_check = [
        "PlayerERA",
        "PlayerBAA",
        "PlayerKs",
        "PlayerBB",
        "PlayerWHIP",
        "PlayerFastballSpeed",
        "PlayerChangeUpSpeed",
        "PlayerIP",
    ]
    return sorted(players, key=lambda x: tuple(safe_float(getattr(x, stat)) for stat in stats_to_check), reverse=True)


def players_catcher_score(players):
    stats_to_check = [
        "PlayerPopTime",
        "ArmVelo"]
    return sorted(players, key=lambda x: tuple(safe_float(getattr(x, stat)) for stat in stats_to_check), reverse=True)