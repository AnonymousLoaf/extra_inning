import os
import pandas as pd
from scoring import (
    players_pitcher_score,
    players_defensive_score,
    players_catcher_score
)

def export_to_excel(players, file, attr_names):
    output_directory = os.path.dirname(file)

    #Pitchers Stats
    pitchers = [player for player in players if player.PlayerPosition == "Pitcher"]
    pitchers = players_pitcher_score(pitchers)
    save_to_excel(pitchers, os.path.join(output_directory, "Pitchers.xlsx"), attr_names)

    # Catchers Stats
    catchers = [player for player in players if player.PlayerPosition == "Catcher"]
    catchers = players_catcher_score(catchers)
    save_to_excel(catchers, os.path.join(output_directory, "Catchers.xlsx"), attr_names)

    # Defense Stats
    defensive_players = [player for player in players if player.PlayerPosition in ["MIF", "CIF", "Outfielder"]]
    defensive_players = players_defensive_score(defensive_players)
    save_to_excel(defensive_players, os.path.join(output_directory, "Defense.xlsx"), attr_names)

def save_to_excel(players, file_path, fieldnames):
    data = [player.__dict__ for player in players]
    df = pd.DataFrame(data, columns=fieldnames)
    df.to_excel(file_path, index=False)