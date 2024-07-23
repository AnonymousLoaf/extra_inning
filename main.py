import os
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedTk
import ttkbootstrap as ttk
import pandas as pd
from get_nominations import ExcelData
from player import Player
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

        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("500x400")
        self.root.style = ttk.Style("darkly")  # Change style here if desired

        # Frame for padding
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = ttk.Label(frame, text="Player Nomination Ranking", font=("",18))
        self.title_label.pack(pady=5)

        self.file_label = ttk.Label(frame, text="Select XLSX File:")
        self.file_label.pack(pady=5)

        self.file_entry = ttk.Entry(frame, width=50)
        self.file_entry.pack(pady=5)

        self.browse_button = ttk.Button(
            frame, text="Browse", command=self.browse_file, bootstyle="info"
        )
        self.browse_button.pack(pady=5)

        self.run_button = ttk.Button(
            frame, text="Run", command=self.run_script, bootstyle="success"
        )
        self.run_button.pack(pady=5)

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

        test_girl = Player()
        for player in players:
            test_in, test_bat = test_girl.calculate_player_score(player)
            print(test_in, test_bat)

        pitchers = [player for player in players if player.PlayerPosition == "Pitcher"]
        pitchers = players_pitcher_score(pitchers)
        self.save_to_excel(
            pitchers,
            os.path.join(output_directory, "Pitchers.xlsx"),
            data.attr_names,
        )

        defensive_players = [
            player
            for player in players
            if player.PlayerPosition in ["MIF", "CIF", "Outfielder"]
        ]
        defensive_players = players_defensive_score(defensive_players)

        # Sorting players by fielding percentage
        defensive_players = sorted(
            defensive_players, key=lambda x: x.FieldingPerc, reverse=True
        )

        self.save_to_excel(
            defensive_players,
            os.path.join(output_directory, "Defense.xlsx"),
            data.attr_names,
        )

        catchers = [player for player in players if player.PlayerPosition == "Catcher"]
        catchers = players_catcher_score(catchers)
        self.save_to_excel(
            catchers,
            os.path.join(output_directory, "Catchers.xlsx"),
            data.attr_names,
        )

        batters = players
        batters = players_batting_score(batters)
        self.save_to_excel(
            batters,
            os.path.join(output_directory, "Batters.xlsx"),
            data.attr_names,
        )

        messagebox.showinfo("Success", "Processing complete.")

    def save_to_excel(self, players, file_path, fieldnames):
        data = [player.__dict__ for player in players]
        df = pd.DataFrame(data, columns=fieldnames)
        df.to_excel(file_path, index=False)


if __name__ == "__main__":

    root = ThemedTk(theme="cosmo")  # Use a ThemedTk for nicer aesthetics
    app = PlayerNominationApp(root)
    root.mainloop()
