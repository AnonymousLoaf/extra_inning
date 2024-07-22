import tkinter as tk
from tkinter import filedialog
from get_nominations import CSVData
from compare import players_pitcher_score, players_defensive_score, players_catcher_score, players_batting_score
import csv
import os

class PlayerNominationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Player Nomination Application")

        self.file_label = tk.Label(self.root, text="Select CSV File:")
        self.file_label.pack()

        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.pack()

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.run_button = tk.Button(self.root, text="Run", command=self.run_script)
        self.run_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def run_script(self):
        file = self.file_entry.get()
        if not os.path.isfile(file):
            tk.messagebox.showerror("Error", f"Cannot find file '{file}'.")
            return

        data = CSVData(file)
        data.load_players()
        data.update_player_attr_names()
        players = data.players

        output_directory = os.path.dirname(file)

        pitchers = [player for player in players if player.PlayerPosition == "Pitcher" or player.PlayerSecondaryPosition == "Pitcher"]
        pitchers = players_pitcher_score(pitchers)
        self.save_to_csv(pitchers, os.path.join(output_directory, "Pitchers.csv"), data.attr_names)

        defensive_players = [player for player in players if player.PlayerPosition in ["MIF", "CIF", "Outfielder"] or player.PlayerSecondaryPosition in ["MIF", "CIF", "Outfielder"]]
        defensive_players = players_defensive_score(defensive_players)
        self.save_to_csv(defensive_players, os.path.join(output_directory, "Defense.csv"), data.attr_names)

        catchers = [player for player in players if player.PlayerPosition == "Catcher" or player.PlayerSecondaryPosition == "Catcher"]
        catchers = players_catcher_score(catchers)
        self.save_to_csv(catchers, os.path.join(output_directory, "Catchers.csv"), data.attr_names)

        batters = players
        batters = players_batting_score(batters)
        self.save_to_csv(batters, os.path.join(output_directory, "Batters.csv"), data.attr_names)

        tk.messagebox.showinfo("Success", "Processing complete.")

    def save_to_csv(self, players, file_path, fieldnames):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for player in players:
                writer.writerow(player.__dict__)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerNominationApp(root)
    root.mainloop()
