from gui import PlayerNominationApp
from load import load_players, get_attr_names
from export import export_to_excel
from player import Player
from ttkthemes import ThemedTk


def run_script(app):
    # Get the file path
    file = app.get_file()

    # Load the data
    players = load_players(file)

    # Calculate player scores
    for player in players:
        Player.calculate_player_score(player)
        print(player.PlayerFirstName, player.PlayerLastName, player.pitching_score)

    # Export to excel
    # export_to_excel(players, file, get_attr_names(file))
    app.finish_message()


if __name__ == "__main__":
    root = ThemedTk(theme="cosmo")  # Use a ThemedTk for nicer aesthetics
    app = PlayerNominationApp(root, run_script)
    root.mainloop()
