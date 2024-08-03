# formatter.py
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


def format_excel(file_path):
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

    for col_idx, column in enumerate(sheet.iter_cols(), start=1):
        color = colors[(col_idx - 1) % len(colors)]
        if (col_idx - 1) % 3 == 0:
            fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            for cell in column:
                cell.fill = fill

    auto_adjust_column_width(sheet)

    workbook.save(file_path)
