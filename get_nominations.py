from extra_inning.player import Player
import csv

class CSVData:
    def __init__(self, file):
        self.file = file
        self.players = []
        self.attr_names = []

    def load_players(self):
        try:
            with open(self.file, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.players.append(Player(**row))
        except FileNotFoundError:
            print(f"File '{self.file}' not found.")
        except Exception as e:
            print(f"Error loading players: {e}")

    def update_attr_names(self, mapping_file):
        try:
            with open(mapping_file, 'r', encoding='utf-8') as file:
                for line in file:
                    old_name, new_name = line.strip().split('--')
                    old_name = old_name.strip()
                    new_name = new_name.strip()
                    self.attr_names.append(new_name)
                    for player in self.players:
                        if hasattr(player, old_name):
                            setattr(player, new_name, getattr(player, old_name))
                            delattr(player, old_name)
        except FileNotFoundError:
            print(f"Mapping file '{mapping_file}' not found.")
        except Exception as e:
            print(f"Error updating attribute names: {e}")

    def get(self, name):
        for player in self.players:
            if player.PlayerName == name:
                return player
        return None