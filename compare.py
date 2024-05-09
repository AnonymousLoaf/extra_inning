def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0

def sort_players_defensive(players):
    return sorted(players, key=lambda x: (safe_float(x.FieldingPerc), safe_float(x.TotalChances), safe_float(x.Assists), safe_float(x.Putouts)), reverse=True)