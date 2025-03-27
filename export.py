import os
import pandas as pd
from formatter import format_excel


def export_to_excel(players, file, selected_options):
    """Should sort each position separately based on their position scores."""
    output_directory = os.path.dirname(file)

    fieldnames = [
    "is_red_flag", "LastYearRank", "RankedThisYear", "WhereToRankRegionallyCoach", "WhereToRankNationallyCoach",
    "PrefferedRecomendation", "Done", "Notes", "PlayerFirstName", "PlayerLastName", 
    "RankedPrevious", "PlayerHometown", "PlayerHighSchool", "x", "PlayerGPA", 
    "PlayerRegion", "PlayerCommitted", "PlayerCommittedTo", "ActionVideo",
    "Slapper", "PlayerPA", "PlayerAB", "PlayerBA", "CalculatedBA", "PlayerOBP", "PlayerOPS", 
    "PlayerHits", "PlayerDoubles", "PlayerTriples", "PlayerHR", "PlayerRBI", 
    "PlayerStrikeOuts", "PlayerPosition", "FieldingPerc", "CalculatedFieldingPerc", "TotalChances", "Assist",
    "Putouts", "PlayerArmVelo", "PlayerERA", "PlayerWHIP", "PlayerKs", 
    "PlayerBB", "PlayerIP", "PlayerBAA", "PlayerFastballSpeed", "PlayerChangeUpSpeed", 
    "PlayerPopTime", "PlayerSB", "PlayerATT", "PlayerAccomplishments", "CoachQuote", 
    "PlayersRecOutsideOrg", "TopTournaments", "WhatElse", "ParentFirstName", "ParentLastName", 
    "ParentEmail", "ParentPhone", "Headshot", "ContactFirstName", "ContactLastName", 
    "ContactEmail", "ContactPhone", "NominatorFirstName", "NominatorLastName", 
    "NominatorEmail", "NominatorPhone", "CoachNameFirst", "CoachNameLast", 
    "CoachEmail", "CoachPhone", "ClubTeamName", "GameChangerName", "AthletesGoLiveName", 
    "OrgLeaderFirstName", "OrgLeaderLastName", "OrgEmail", "OrgPhone", "pos_batting_rank", "global_batting_rank", "num_national_tournament"
    ]

    # Pitchers Stats
    if selected_options["pitchers"]:
        pitch_fieldnames = fieldnames.copy()
        pitchers = [player for player in players if player.PlayerPosition == "Pitcher"]
        sorted_pitchers = sorted(
            pitchers, key=lambda player: player.pitching_score, reverse=True
        )
        # Add pitching score to atter names
        if "pitching_score" not in pitch_fieldnames:
            pitch_fieldnames.append("pitching_score")
        if "batting_score" not in pitch_fieldnames:
            pitch_fieldnames.append("batting_score")
        # Save pitchers to excel, independent from other positions
        save_to_excel(
            sorted_pitchers,
            os.path.join(output_directory, "Pitchers.xlsx"),
            pitch_fieldnames,
            "pitching_score",
        )
        format_excel(
            os.path.join(output_directory, "Pitchers.xlsx"),
        )

    # Catchers Stats
    if selected_options["catchers"]:
        catch_fieldnames = fieldnames.copy()
        if "catching_score" not in catch_fieldnames:
            catch_fieldnames.append("catching_score")
        if "batting_score" not in catch_fieldnames:
            catch_fieldnames.append("batting_score")
        if "catcher_score" not in catch_fieldnames:
            catch_fieldnames.append("catcher_score")

        catchers = [player for player in players if player.PlayerPosition == "Catcher"]
        sorted_catchers = sorted(
            catchers, key=lambda player: player.catcher_score, reverse=True
        )
        save_to_excel(
            sorted_catchers,
            os.path.join(output_directory, "Catchers.xlsx"),
            catch_fieldnames,
            "catcher_score",
        )
        format_excel(
            os.path.join(output_directory, "Catchers.xlsx"),
        )

    # Infielder Stats
    if selected_options["infield"]:
        infield_fieldnames = fieldnames.copy()
        if "infield_score" not in infield_fieldnames:
            infield_fieldnames.append("infield_score")
        if "batting_score" not in infield_fieldnames:
            infield_fieldnames.append("batting_score")

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
            infield_fieldnames,
            "infielder_score",
        )
        format_excel(
            os.path.join(output_directory, "Infielders.xlsx"),
        )

    # Outfield Stats
    if selected_options["outfield"]:
        outfield_fieldnames = fieldnames.copy()
        if "outfield_score" not in outfield_fieldnames:
            outfield_fieldnames.append("outfield_score")
        if "batting_score" not in outfield_fieldnames:
            outfield_fieldnames.append("batting_score")

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
            outfield_fieldnames,
            "outfield_score",
        )
        format_excel(
            os.path.join(output_directory, "Outfielder.xlsx"),
        )

    # Batting Stats
    if selected_options["batting"]:
        batting_fieldnames = fieldnames.copy()
        if "batting_score" not in batting_fieldnames:
            batting_fieldnames.append("batting_score")
        batters = [player for player in players]
        sorted_batters = sorted(
            batters, key=lambda player: player.batting_score, reverse=True
        )
        save_to_excel(
            sorted_batters, os.path.join(output_directory, "Batters.xlsx"), batting_fieldnames, "batting_score"
        )
        format_excel(
            os.path.join(output_directory, "Batters.xlsx"),
        )

    # GPA Stats
    if selected_options["gpa"]:
        gpa_fieldnames = fieldnames.copy()
        save_to_excel(
            players, os.path.join(output_directory, "GPA.xlsx"), gpa_fieldnames, "PlayerGPA"
        )
        format_excel(
            os.path.join(output_directory, "GPA.xlsx"),
        )


def save_to_excel(players, file_path, fieldnames, score_column):
    """Saves players to excel file based on their position."""
    print(f"Ranking and exporting {file_path.split('\\')[-1]}...")

    for player in players:
        if 'PlayerCommitted' not in player.__dict__:
            player.PlayerCommitted = None
        if 'GameChangerName' not in player.__dict__:
            player.GameChangerName = None

    data = [player.__dict__ for player in players]
    df = pd.DataFrame(data)

    # Check if all fieldnames exist in the DataFrame
    missing_columns = [col for col in fieldnames if col not in df.columns]

    # Handle missing columns by filling with default values (e.g., None)
    if missing_columns:
        print(f"Warning: The following columns are missing from the data and will be filled with None: {missing_columns}")
        for col in missing_columns:
            df[col] = None

    # Reorder the DataFrame according to fieldnames ensuring all are included
    df = df[fieldnames]

    # Sort by score_column if it's one of the fieldnames
    if score_column in fieldnames:
        df = df.sort_values(by=score_column, ascending=False)

    # Export to Excel
    df.to_excel(file_path, index=False)
