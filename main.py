from gui import PlayerNominationApp
from load import load_players
from export import export_to_excel
from ttkthemes import ThemedTk
import os

def run_script(app):
    # Get the file path
    file = app.get_file()

    # Load the data
    players, attr_names = load_players(file)

    selected_options = app.get_selected_options()

    # Calculate player scores
    for player in players:
        if should_process_player(player, selected_options):
            player.calculate_player_score()

    # Export to excel
    export_to_excel(players, file, selected_options)

    err_dir = os.path.dirname(file)
    all_errors = []
    error_count = 0

    for player in players:
        if player.error_list:
            all_errors.extend(player.error_list)
            error_count += len(player.error_list)

    warnings_file_path = os.path.join(err_dir, 'warnings_report.txt')
    with open(warnings_file_path, 'w') as file:
        for error in all_errors:
            file.write(error + '\n')

    print(f"Total number of warnings found: {error_count}")
    with open(warnings_file_path, 'a') as file:
        file.write(f"\nTotal number of warnings: {error_count}")

def should_process_player(player, options):
    if options['pitchers'] and player.PlayerPosition == 'Pitcher':
        return True
    if options['catchers'] and player.PlayerPosition == 'Catcher':
        return True
    if options['infield'] and player.PlayerPosition in ["Infielder", "IF", "1B", "2B", "3B", "SS", "CIF", "MIF"]:
        return True
    if options['outfield'] and player.PlayerPosition == "Outfielder":
        return True
    if options['batting'] and hasattr(player, 'batting_score'):
        return True
    if options['gpa'] and hasattr(player, 'gpa'):
        return True
    return False

if __name__ == "__main__":
    root = ThemedTk(theme="cosmo")  # Use a ThemedTk for nicer aesthetics
    app = PlayerNominationApp(root, run_script)
    root.mainloop()
