import os
from gui import PlayerNominationApp
from load import load_players, get_attr_names
from export import export_to_excel
from ttkthemes import ThemedTk

def run_script(app):
    # Get the file path
    file = app.get_file()
    if not os.path.isfile(file):
        app.error_message("file")
        return
    elif not file.endswith(".xlsx"):
        app.error_message("wrongFile")
        return

    # Load the data
    players = load_players(file)

    # Calculate player scores
    for player in players:
        player.calculate_player_score()

    # Export to excel
    export_to_excel(players, file, get_attr_names(file))
    app.finish_message()


if __name__ == "__main__":
    root = ThemedTk(theme="cosmo")  # Use a ThemedTk for nicer aesthetics
    app = PlayerNominationApp(root, run_script)
    root.mainloop()  # Start the GUI application
    run_script(app)
    
