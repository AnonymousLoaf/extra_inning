import os
import pandas as pd
from formatter import format_excel


def export_to_excel(players, file, attr_names):
    """Should sort each position separately based on their position scores."""
    output_directory = os.path.dirname(file)

    # Pitchers Stats
    # Get and sort the pitchers
    pitchers = [player for player in players if player.PlayerPosition == "Pitcher"]
    sorted_pitchers = sorted(
        pitchers, key=lambda player: player.pitching_score, reverse=True
    )
    # Save OG attr names
    attr_names_copy = attr_names.copy()

    # Add pitching score to atter names
    if "pitching_score" not in attr_names_copy:
        attr_names_copy.append("pitching_score")

    # Save pitchers to excel, independent from other positions
    save_to_excel(
        sorted_pitchers,
        os.path.join(output_directory, "Pitchers.xlsx"),
        attr_names_copy,
    )
    format_excel(
        os.path.join(output_directory, "Pitchers.xlsx"),
    )

    # Catchers Stats
    attr_names_copy = attr_names.copy()
    if "catching_score" not in attr_names_copy:
        attr_names_copy.append("catching_score")
    catchers = [player for player in players if player.PlayerPosition == "Catcher"]
    sorted_catchers = sorted(
        catchers, key=lambda player: player.catching_score, reverse=True
    )
    save_to_excel(
        sorted_catchers,
        os.path.join(output_directory, "Catchers.xlsx"),
        attr_names_copy,
    )
    format_excel(
        os.path.join(output_directory, "Catchers.xlsx"),
    )

    # Defense Stats
    attr_names_copy = attr_names.copy()
    if "defensive_score" not in attr_names_copy:
        attr_names_copy.append("defensive_score")
    defensive_players = [
        player
        for player in players
        if player.PlayerPosition in ["MIF", "CIF", "Outfielder", "Infielder"]
    ]
    sorted_defensive_players = sorted(
        defensive_players, key=lambda player: player.defensive_score, reverse=True
    )
    save_to_excel(
        sorted_defensive_players,
        os.path.join(output_directory, "Defense.xlsx"),
        attr_names_copy,
    )
    format_excel(
        os.path.join(output_directory, "Defense.xlsx"),
    )

    # Batting Stats
    attr_names_copy = attr_names.copy()
    if "batting_score" not in attr_names_copy:
        attr_names_copy.append("batting_score")
    batters = [player for player in players]
    sorted_batters = sorted(
        batters, key=lambda player: player.batting_score, reverse=True
    )
    save_to_excel(
        sorted_batters, os.path.join(output_directory, "Batters.xlsx"), attr_names_copy
    )
    format_excel(
        os.path.join(output_directory, "Batters.xlsx"),
    )


def save_to_excel(players, file_path, fieldnames):
    """Saves players to excel file based on their position."""
    data = [player.__dict__ for player in players]
    df = pd.DataFrame(data, columns=fieldnames)

    # Sorting DataFrame based on the relevant score
    score_columns = [
        "pitching_score",
        "catching_score",
        "defensive_score",
        "batting_score",
    ]
    for score_column in score_columns:
        if score_column in df.columns:
            df = df.sort_values(by=score_column, ascending=False)

    df.to_excel(file_path, index=False)