from gui import PlayerNominationApp
from load import load_players
from export import export_to_excel
from ttkthemes import ThemedTk


def run_script(app):
    # Get the file path
    file = app.get_file()

    # Load the data
    players, attr_names = load_players(file)

    # Calculate player scores
    for player in players:
        player.calculate_player_score()
        if player.error_list:
            print("\n".join(player.error_list))

    # Export to excel
    export_to_excel(players, file, attr_names)
    app.finish_message()


if __name__ == "__main__":
    root = ThemedTk(theme="cosmo")  # Use a ThemedTk for nicer aesthetics
    app = PlayerNominationApp(root, run_script)
    root.mainloop()
