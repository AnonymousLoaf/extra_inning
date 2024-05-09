from get_nominations import CSVData
from compare import sort_players_defensive
import csv
import os

if __name__ == "__main__":
    file = "C:/Users/theda/Desktop/PlayerNomination/extra_inning/player-coach-nominations-raw.csv"
    mapping_file = "C:/Users/theda/Desktop/PlayerNomination/extra_inning/mapping.txt"
    players = None

    if not os.path.isfile(file):
        print(f"Cannot fine file '{file}'.")
    elif not os.path.isfile(mapping_file):
        print(f"Cannot find mapping file '{mapping_file}'.")
    else:
        data = CSVData(file)
        data.load_players()
        data.update_attr_names(mapping_file)
        players = data.players

    if players:
        for player in players:
            player.clean()

    players = sort_players_defensive(players)

    for player in players:
        if player.PlayerPosition == "Pitcher":
            print(f'Player: {player.PlayerName:<20} Fielding%: {player.FieldingPerc:<10} Total Chances: {player.TotalChances:<10} Assists: {player.Assists:<10} Putouts: {player.Putouts:<10}')

    output_file = "sorted_players.csv"
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.attr_names)
        for player in players:
            player_data = []
            for attr in data.attr_names:
                if hasattr(player, attr):
                    player_data.append(getattr(player, attr))
                else:
                    player_data.append(None)
            writer.writerow(player_data)
            
    print(f"Sorted players are saved in {output_file}.")