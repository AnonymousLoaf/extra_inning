import openpyxl
from openpyxl.styles import PatternFill


def auto_adjust_column_width(sheet):
    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter  # Get the column name
        for cell in column:
            try:
                max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        adjusted_width = max_length + 2
        sheet.column_dimensions[column_letter].width = adjusted_width


def set_fixed_column_width(sheet, width=14):
    for column in sheet.columns:
        column_letter = column[0].column_letter  # Get the column name
        sheet.column_dimensions[column_letter].width = width


def format_excel(file_path):
    # Define the groups of columns
    groups = [
        ["PlayerFirstName", "PlayerLastName"],
        ["Notes"],
        ["PlayerPosition"],
        ["ClubTeamName"],
        ["GameChanger Name"],
        ["PlayerPreviousRanked", "PlayerRanking"],
        [
            "PlayerHometown",
            "HS",
            "PlayerTwitter",
            "PlayerGPA",
            "PlayerRegion",
            "PlayerCommitted",
            "PlayerUniversity",
            "ActionVideo",
        ],
        [
            "Slapper",
            "PlayerPA",
            "PlayerAB",
            "PlayerBA",
            "PlayerOBP",
            "PlayerOPS",
            "PlayerHits",
            "PlayerDoubles",
            "PlayerTriples",
            "PlayerHR",
            "PlayerRBI",
            "PlayerStrikeOuts",
        ],
        [
            "FieldingPerc",
            "TotalChances",
            "Assist",
            "Putouts",
            "PlayerArmVelo",
        ],
        [
            "PlayerERA",
            "PlayerWHIP",
            "PlayerKs",
            "PlayerBB",
            "PlayerIP",
            "PlayerBAA",
            "PlayerFastballSpeed",
            "PlayerChangeUpSpeed",
        ],
        [
            "PlayerPopTime",
            "PlayerArmVelo",
            "PlayerSB",
            "PlayerATT",
            "FieldingPerc",
        ],
        [
            "CoachRecommend50",
            "PlayerRankingEstimate",
        ],
        [
            "PlayerAccomplishments",
            "PlayerQuote",
        ],
        [
            "Top3Org",
            "Top Tournaments",
        ],
        [
            "Else",
        ],
        [
            "Parent1Name",
            "Parent1Email",
            "Parent1Phone",
            "Parent2Name",
            "Parent2Email",
            "Parent2Phone",
        ],
        [
            "Headshot",
        ],
        [
            "ContactFirstName",
            "ContactLastName",
            "ContactEmail",
            "ContactPhone",
        ],
        [
            "NominatorName",
            "NaminatorNameLast",
            "NominatorEmail",
            "NominatorPhone",
        ],
        [
            "CoachNameFirst",
            "CoachNameLast",
            "CoachEmail",
            "CoachPhone",
        ],
        [
            "AthleteTeamPage",
        ],
        [
            "OrgLeader",
            "OrgEmail",
            "OrgPhone",
        ],
    ]

    # Define the colors for the groups
    colors = [
        "FFFFE0E0",  # Lite Red
        "FFFFE0B2",  # Lite Orange
        "FFFFFFE0",  # Lite Yellow
        "FFE0FFE0",  # Lite Green
        "FFE0FFFF",  # Lite Cyan
        "FFE0E0FF",  # Lite Blue
        "FFFFE0FF",  # Lite Purple
    ]

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Apply colors to the groups
    for group_idx, group in enumerate(groups):
        color = colors[group_idx % len(colors)]
        fill = PatternFill(start_color=color, end_color=color, fill_type="solid")

        for col_name in group:
            col_idx = None
            for cell in sheet[1]:  # Assumes first row contains headers
                if cell.value == col_name:
                    col_idx = cell.column
                    break
            if col_idx is not None:
                for cell in sheet.iter_cols(min_col=col_idx, max_col=col_idx):
                    for single_cell in cell:
                        single_cell.fill = fill

    set_fixed_column_width(sheet)
    workbook.save(file_path)
