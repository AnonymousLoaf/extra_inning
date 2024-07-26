from get_nominations import ExcelData

def load_players(file):
    data = ExcelData(file)
    data.load_players()
    players = data.players
    return players

def get_attr_names(file):
    return ExcelData(file).attr_names