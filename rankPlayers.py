import player

def rank_players(players):
    players.sort(key=lambda p: p.pitching_score + p.catching_score + p.defensive_score + p.batting_score, reverse=True)
    for i, player in enumerate(players):
        player.rank = i + 1
