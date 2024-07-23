import pandas as pd
from player import Player


class ExcelData:
    def __init__(self, file):
        self.file = file
        self.players = []
        self.attr_names = []

    def load_players(self):
        try:
            df = pd.read_excel(self.file)
            for _, row in df.iterrows():
                self.players.append(Player(**row.to_dict()))
        except FileNotFoundError:
            print(f"File '{self.file}' not found.")
        except Exception as e:
            print(f"Error loading players: {e}")

    def update_player_attr_names(self):
        for player in self.players:
            for old_name, new_name in self.attr_mapping.items():
                if hasattr(player, old_name):
                    setattr(player, new_name, getattr(player, old_name))
                    delattr(player, old_name)
        self.attr_names = list(self.attr_mapping.values())

    def get(self, name):
        for player in self.players:
            if player.PlayerFirstName + " " + player.PlayerLastName == name:
                return player
        return None

    attr_mapping = {
        "Name of player (First)": "PlayerFirstName",
        "Name of player (Last)": "PlayerLastName",
        "Has this player been ranked before? If yes, provide rankings # & what year.": "PlayerRanking",
        "Club Coach Name (First)": "ClubCoachFirstName",
        "Club Coach Name (Last)": "ClubCoachLastName",
        "Club Coach Email": "ClubCoachEmail",
        "Club Coach Phone Number": "ClubCoachPhone",
        "Club Team Name": "ClubTeamName",
        "Organization Point of Contact Name": "OrganizationContactName",
        "Organization Point of Contact Phone Number": "OrganizationContactPhone",
        "Game Changer Team Name": "GameChangerTeamName",
        "Primary Position of Player": "PlayerPosition",
        "High School Name": "HighSchoolName",
        "Batting Avg.": "PlayerBA",
        "OBP": "PlayerOBP",
        "OPS": "PlayerOPS",
        "QAB%": "PlayerQAB",
        "Fielding %": "FieldingPerc",
        "TCs": "TotalChances",
        "Assists": "Assist",
        "Pos": "Putouts",
        "Arm Velo": "ArmVelo",
        "ERA": "PlayerERA",
        "WHIP": "PlayerWHIP",
        "Ks": "PlayerKs",
        "BB": "PlayerBB",
        "IP": "PlayerIP",
        "BAA": "PlayerBAA",
        "P's fastball speed?": "PlayerFastballSpeed",
        "Ps change-up speed?": "PlayerChangeUpSpeed",
        " pop-time?": "PlayerPopTime",
        " arm velo?": "ArmVelo2",
        "Coach: where to rank?": "PlayerRankingEstimate",
        "Share this players individual accomplishments (List in bulleted format)": "PlayerAccomplishments",
        "List 3 top events & 3 top opponents": "PlayerEventsandOpponents",
        "Region": "PlayerRegion",
        "Instagram": "PlayerInstagram",
        "Twitter  ": "PlayerTwitter",
        "Parent name": "ParentName",
        "Parent email": "ParentEmail",
        "Parent phone": "ParentPhone",
        "Player Hometown/State": "PlayerHometown",
        "Coach Quote": "PlayerQuote",
        "Headshot": "PlayerHeadshot",
    }
