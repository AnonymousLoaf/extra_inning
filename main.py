import os
import tkinter as tk
import pandas as pd
from tkinter import filedialog, messagebox
from get_nominations import ExcelData
from compare import (
    players_pitcher_score,
    players_defensive_score,
    players_catcher_score,
    players_batting_score,
)


class PlayerNominationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Player Nomination Application")

        self.file_label = tk.Label(self.root, text="Select XLSX File:")
        self.file_label.pack()

        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.pack()

        self.browse_button = tk.Button(
            self.root, text="Browse", command=self.browse_file
        )
        self.browse_button.pack()

        self.run_button = tk.Button(self.root, text="Run", command=self.run_script)
        self.run_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def run_script(self):
        file = self.file_entry.get()
        if not os.path.isfile(file):
            messagebox.showerror("Error", f"Cannot find file '{file}'.")
            return

        data = ExcelData(file)
        data.load_players()
        data.update_player_attr_names()
        players = data.players

        output_directory = os.path.dirname(file)

        find = "Mady Rhone"
        
        player = data.get(find)
        if player is None:
            messagebox.showerror("Error", f"Cannot find player '{find}'.")
            return

        pitchers = [
            player
            for player in players
            if player.PlayerPosition == "Pitcher"
        ]
        pitchers = players_pitcher_score(pitchers)
        self.save_to_excel(
            pitchers, os.path.join(output_directory, "Pitchers.xlsx"), data.attr_names
        )

        defensive_players = [
            player
            for player in players
            if player.PlayerPosition in ["MIF", "CIF", "Outfielder"]
        ]
        defensive_players = players_defensive_score(defensive_players)
        self.save_to_excel(
            defensive_players,
            os.path.join(output_directory, "Defense.xlsx"),
            data.attr_names,
        )

        catchers = [
            player
            for player in players
            if player.PlayerPosition == "Catcher"
        ]
        catchers = players_catcher_score(catchers)
        self.save_to_excel(
            catchers, os.path.join(output_directory, "Catchers.xlsx"), data.attr_names
        )

        batters = players
        batters = players_batting_score(batters)
        self.save_to_excel(
            batters, os.path.join(output_directory, "Batters.xlsx"), data.attr_names
        )

        messagebox.showinfo("Success", "Processing complete.")

    def save_to_excel(self, players, file_path, fieldnames):
        data = [player.__dict__ for player in players]
        df = pd.DataFrame(data, columns=fieldnames)
        df.to_excel(file_path, index=False)


if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerNominationApp(root)
    root.mainloop()
