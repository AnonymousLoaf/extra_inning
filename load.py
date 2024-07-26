from get_nominations import ExcelData

def load_players(file):
    data = ExcelData(file)
    data.load_players()
    data.update_player_attr_names()
    players = data.players
    return players

def get_attr_names(file):
    data = ExcelData(file)
    data.load_players()
    data.update_player_attr_names()
    return data.attr_names