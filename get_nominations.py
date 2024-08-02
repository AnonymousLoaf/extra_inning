import pandas as pd
from player import Player


class ExcelData:
    def __init__(self, file):
        self.file = file
        self.players = []
        self.attr_names = []

    def map_column(self, column_name):
        keyword_mappings = {
            "PlayerFirstName": ["name", "first", "player", "player"],
            "PlayerLastName": ["name", "last", "player", "player"],
            "PlayerRanking": ["rank", "ranked"],
            "ClubCoachFirstName": ["coach", "first"],
            "ClubCoachLastName": ["coach", "last"],
            "ClubCoachEmail": ["coach", "email"],
            "ClubCoachPhone": ["coach", "phone"],
            "ClubTeamName": ["team", "name"],
            "OrganizationContactName": ["contact", "name"],
            "OrganizationContactPhone": ["contact", "phone"],
            "GameChangerTeamName": ["game", "changer", "team"],
            "PlayerPosition": ["position"],
            "HighSchoolName": ["high", "school"],
            "PlayerBA": ["batting", "avg"],
            "PlayerOBP": ["obp"],
            "PlayerOPS": ["ops"],
            "PlayerQAB": ["qab%"],
            "FieldingPerc": ["fielding", "%"],
            "TotalChances": ["tcs"],
            "Assist": ["assists"],
            "Putouts": ["pos"],
            "PlayerArmVelo": ["arm", "velo"],
            "PlayerERA": ["era"],
            "PlayerWHIP": ["whip"],
            "PlayerKs": ["ks"],
            "PlayerBB": ["bb"],
            "PlayerIP": ["ip"],
            "PlayerBAA": ["baa"],
            "PlayerFastballSpeed": ["fastball", "speed"],
            "PlayerArmVelo2": ["arm", "velo"],
            "PlayerChangeUpSpeed": ["change", "speed"],
            "PlayerPopTime": ["pop", "time"],
            "PlayerArmVelo": ["arm", "velo"],
            "PlayerRankingEstimate": ["rank", "estimate"],
            "PlayerAccomplishments": ["accomplishments"],
            "PlayerEventsandOpponents": ["events", "opponents"],
            "PlayerRegion": ["region"],
            "PlayerInstagram": ["instagram"],
            "PlayerTwitter": ["twitter"],
            "ParentName": ["parent", "name"],
            "ParentEmail": ["parent", "email"],
            "ParentPhone": ["parent", "phone"],
            "PlayerHometown": ["hometown", "state"],
            "PlayerQuote": ["quote"],
            "PlayerHeadshot": ["headshot"]
        }

        for standard_key, keywords in keyword_mappings.items():
            if all(keyword in column_name.lower() for keyword in keywords):
                return standard_key
        return column_name

    def load_players(self):
        try:
            df = pd.read_excel(self.file)
            df.rename(columns=lambda x: self.map_column(x), inplace=True)
            self.attr_names = df.columns.tolist()
            for _, row in df.iterrows():
                self.players.append(Player(**row.to_dict()))
        except FileNotFoundError:
            print(f"File '{self.file}' not found.")
        except Exception as e:
            print(f"Error loading players: {e}")

    def get(self, name):
        for player in self.players:
            full_name = player.PlayerFirstName + " " + player.PlayerLastName
            if full_name == name:
                return player
        return None
