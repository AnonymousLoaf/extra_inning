from get_nominations import ExcelData


def load_players(file):
    data = ExcelData(file)
    data.make_players()
    data.calculate_player_fielding_percent()
    data.calculate_player_batting_avg()
    data.check_players()
    players = data.players
    return players, data.attr_names


def get_attr_names(file):
    return ExcelData(file).attr_names
