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
        pitchers, key=lambda player: player.pitcher_score, reverse=True
    )

    if "FieldingPerc" in attr_names:
        attr_names.remove("FieldingPerc")
        attr_names.insert(42, "FieldingPerc")
    if "PlayerArmVelo" in attr_names:
        attr_names.remove("PlayerArmVelo")
        attr_names.insert(40, "PlayerArmVelo")

    # Save OG attr names
    attr_names_copy = attr_names.copy()

    # Add pitching score to atter names
    if "pitching_score" not in attr_names_copy:
        attr_names_copy.append("pitching_score")
        attr_names_copy.append("batting_score")
        attr_names_copy.append("pitcher_score")

    # Save pitchers to excel, independent from other positions
    save_to_excel(
        sorted_pitchers,
        os.path.join(output_directory, "Pitchers.xlsx"),
        attr_names_copy,
        "pitcher_score",
    )
    format_excel(
        os.path.join(output_directory, "Pitchers.xlsx"),
    )

    # Catchers Stats
    attr_names_copy = attr_names.copy()
    if "catching_score" not in attr_names_copy:
        attr_names_copy.append("catching_score")
        attr_names_copy.append("batting_score")
        attr_names_copy.append("catcher_score")

    catchers = [player for player in players if player.PlayerPosition == "Catcher"]
    sorted_catchers = sorted(
        catchers, key=lambda player: player.catcher_score, reverse=True
    )
    save_to_excel(
        sorted_catchers,
        os.path.join(output_directory, "Catchers.xlsx"),
        attr_names_copy,
        "catcher_score",
    )
    format_excel(
        os.path.join(output_directory, "Catchers.xlsx"),
    )

    # Infielder Stats
    attr_names_copy = attr_names.copy()
    if "infield_score" not in attr_names_copy:
        attr_names_copy.append("infield_score")
        attr_names_copy.append("batting_score")

    defensive_players = [
        player
        for player in players
        if player.PlayerPosition in ["Infielder", "IF", "1B", "2B", "3B", "SS", "CIF", "MIF"]
    ]
    sorted_defensive_players = sorted(
        defensive_players, key=lambda player: player.infield_score, reverse=True
    )
    save_to_excel(
        sorted_defensive_players,
        os.path.join(output_directory, "Infielders.xlsx"),
        attr_names_copy,
        "infielder_score",
    )
    format_excel(
        os.path.join(output_directory, "Infielders.xlsx"),
    )

    # outfield Stats
    attr_names_copy = attr_names.copy()
    if "outfield_score" not in attr_names_copy:
        attr_names_copy.append("outfield_score")
        attr_names_copy.append("batting_score")

    defensive_players = [
        player
        for player in players
        if player.PlayerPosition in ["Outfielder"]
    ]
    sorted_defensive_players = sorted(
        defensive_players, key=lambda player: player.outfield_score, reverse=True
    )
    save_to_excel(
        sorted_defensive_players,
        os.path.join(output_directory, "Outfielder.xlsx"),
        attr_names_copy,
        "outfield_score",
    )
    format_excel(
        os.path.join(output_directory, "Outfielder.xlsx"),
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
        sorted_batters, os.path.join(output_directory, "Batters.xlsx"), attr_names_copy, "batting_score"
    )
    format_excel(
        os.path.join(output_directory, "Batters.xlsx"),
    )

    # Red Flags
    attr_names_copy = attr_names.copy()
    if "is_red_flag" not in attr_names_copy:
        attr_names_copy.insert(0, "is_red_flag")
    red_flags = [player for player in players if player.is_red_flag]
    save_to_excel(
        red_flags, os.path.join(output_directory, "RedFlags.xlsx"), attr_names_copy, "is_red_flag"
    )
    format_excel(
        os.path.join(output_directory, "RedFlags.xlsx"),
    )


def save_to_excel(players, file_path, fieldnames, score_column):
    """Saves players to excel file based on their position."""
    data = [player.__dict__ for player in players]
    df = pd.DataFrame(data, columns=fieldnames)

    if score_column in df.columns:
        df = df.sort_values(by=score_column, ascending=False)

    df.to_excel(file_path, index=False)
