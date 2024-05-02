from extra_inning.get_nominations import CSVData
import csv
import os

def calculate_player_score(player):
    if player.PlayerPosition == "Pitcher":
        return 0
    else:
        #infield_stats = sum([getattr(player, arg, 0) for arg in ['TotalChances', 'Assists', 'Putouts', 'FieldingPerc'] if isinstance(getattr(player, arg, 0), (int, float))])
        batting_stats = sum([getattr(player, arg, 0) for arg in ['OBP', 'OPS', 'QAB'] if isinstance(getattr(player, arg, 0), (int, float))])
        return batting_stats

if __name__ == "__main__":
    file = "player-coach-nominations-raw.csv"
    mapping_file = "mapping.txt"
    players = None

    if not os.path.isfile(file) or not os.path.isfile(mapping_file):
        print("Required files not found.")
    else:
        data = CSVData(file)
        data.load_players()
        data.update_attr_names(mapping_file)
        players = data.players

    if players:
        for player in players:
            player.clean()

    sorted_players = sorted(players, key=calculate_player_score, reverse=True)

    output_file = "sorted_players.csv"
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Score'] + data.attr_names)
        for player in sorted_players:
            player_data = [calculate_player_score(player)]
            for attr in data.attr_names:
                if hasattr(player, attr):
                    player_data.append(getattr(player, attr))
                else:
                    player_data.append(None)
            writer.writerow(player_data)
            
    print(f"Sorted players are saved in {output_file}.")
