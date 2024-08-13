# Example stats for multiple players
players_stats = [
    {
        "name": "Player 1",
        "ERA": 2.25,
        "WHIP": 1.1,
        "Ks": 83,
        "BB": 40,
        "IP": 85,
        "BAA": 0.22,
    },
    {
        "name": "Player 2",
        "ERA": 3.1,
        "WHIP": 1.6,
        "Ks": 50,
        "BB": 10,
        "IP": 170,
        "BAA": 0.197,
    },
    {
        "name": "Player 3",
        "ERA": 0.816,
        "WHIP": 0.864,
        "Ks": 197,
        "BB": 36,
        "IP": 103,
        "BAA": 0.146,
    },
    {
        "name": "Player 4",
        "ERA": 1.192,
        "WHIP": 1.1,
        "Ks": 80,
        "BB": 10,
        "IP": 200,
        "BAA": 1,
    },
    {
        "name": "Player 5",
        "ERA": 1.842,
        "WHIP": 1.018,
        "Ks": 156,
        "BB": 37,
        "IP": 114,
        "BAA": 0.189,
    },
]

# Weight dictionary based on your provided weights
weights = {
    "ERA": 1.00,
    "WHIP": 0.95,
    "BAA": 0.90,
    "Ks": 0.85,
    "IP": 0.80,
    "BB": 0.75,
}


# Scaling function for stats that should be low
def scale_stat(stat):
    return 1000 / (stat + 1000)


# Scaling function for stats that should be high
def scale_stat_high(stat):
    return 1000 / (1100 - stat)


# Calculate final score for each player and store results
player_scores = []
for player in players_stats:
    final_score = 0
    for stat in weights:
        if stat in ["Ks", "IP"]:
            final_score += scale_stat_high(player[stat]) * weights[stat]
        else:
            final_score += scale_stat(player[stat]) * weights[stat]
    player_scores.append({"name": player["name"], "score": final_score})

# Sort players by final score in ascending order (best to worst)
player_scores = sorted(player_scores, key=lambda x: x["score"], reverse=True)

# Print the rankings
for idx, player in enumerate(player_scores, start=1):
    print(f"Rank {idx}: {player['name']} with a score of {player['score']:.4f}")
