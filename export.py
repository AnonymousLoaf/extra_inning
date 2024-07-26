import os
import pandas as pd
from scoring import (
    player_pitching_score,
    player_defense_score,
    player_catching_score,
    player_batting_score,
)


def export_to_excel(players, file, attr_names):
    output_directory = os.path.dirname(file)

    # Pitchers Stats
    pitchers = [player for player in players if player.PlayerPosition == "Pitcher"]
    pitchers = player_pitching_score(pitchers)
    save_to_excel(pitchers, os.path.join(output_directory, "Pitchers.xlsx"), attr_names)

    # Catchers Stats
    catchers = [player for player in players if player.PlayerPosition == "Catcher"]
    catchers = player_catching_score(catchers)
    save_to_excel(catchers, os.path.join(output_directory, "Catchers.xlsx"), attr_names)

    # Defense Stats
    defensive_players = [
        player
        for player in players
        if player.PlayerPosition in ["MIF", "CIF", "Outfielder"]
    ]
    defensive_players = player_defense_score(defensive_players)
    save_to_excel(
        defensive_players, os.path.join(output_directory, "Defense.xlsx"), attr_names
    )


    # Batting Stats
    batters = [player for player in players]
    batters = player_batting_score(batters)
    save_to_excel(batters, os.path.join(output_directory, "Batters.xlsx"), attr_names)

    # Batting Stats
    batters = [player for player in players]
    batters = player_batting_score(batters)
    save_to_excel(batters, os.path.join(output_directory, "Batters.xlsx"), attr_names)

def save_to_excel(players, file_path, fieldnames):
    data = [player.__dict__ for player in players]
    df = pd.DataFrame(data, columns=fieldnames)
    df.to_excel(file_path, index=False)
