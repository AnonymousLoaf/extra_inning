import os
from gui import PlayerNominationApp as PA
from load import load_players, get_attr_names
from export import export_to_excel
from ttkthemes import ThemedTk

def run_script(self):
    #Get the file path
    file = self.file_entry.get()
    if not os.path.isfile(file):
        PA.error_message("file")
        return
    elif not file.endswith(".xlsx"):
        PA.error_message("wrongFile")
        return

    #Load the data
    players = load_players(file)

    #Calculate player scores
    for player in players:
        player.calculate_score()

    #export to excel
    export_to_excel(players, file, get_attr_names(file))
    PA.finish_message()


if __name__ == "__main__":
    root = ThemedTk(theme="cosmo")  # Use a ThemedTk for nicer aesthetics
    app = PA(root, run_script)
    root.mainloop()
