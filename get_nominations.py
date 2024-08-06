import pandas as pd
from player import Player


class ExcelData:
    def __init__(self, file):
        self.file = file
        self.players = []
        self.attr_names = []

    def map_column(self, column_name):
        keyword_mappings = {
            "PlayerFirstName": ["name", "first", "player"],
            "PlayerLastName": ["name", "last", "player"],
            "Notes": ["notes"],
            "PlayerPosition": ["primary", "position"],
            "ClubTeamName": ["team", "name"],
            "GameChangerName": ["game", "changer"],
            "PlayerPreviousRanked": ["previously", "ranked"],
            "PlayerRanking": ["ranking"],
            "PlayerHometown": ["hometown"],
            "HighSchoolName": ["high", "school", "hs"],
            "PlayerTwitter": ["twitter"],
            "PlayerGPA": ["gpa"],
            "PlayerRegion": ["region"],
            "PlayerCommitted": ["committed"],
            "PlayerUniversity": ["university"],
            "ActionVideo": ["action", "video"],
            "Slapper": ["slapper"],
            "PlayerPA": ["pa"],
            "PlayerAB": ["at", "bats", "ab"],
            "PlayerBA": ["batting", "avg"],
            "PlayerOBP": ["obp"],
            "PlayerOPS": ["ops"],
            "PlayerHits": ["hits"],
            "PlayerDoubles": ["doubles"],
            "PlayerTriples": ["triples"],
            "PlayerHR": ["homeruns", "hr"],
            "PlayerRBI": ["rbi"],
            "PlayerStrikeOuts": ["strikeouts"],
            "FieldingPerc": ["fielding", "%"],
            "TotalChances": ["tcs"],
            "Assist": ["assists"],
            "Putouts": ["pos"],
            "PlayerArmVelo": ["arm", "velo"],
            "PlayerERA": ["era"],
            "PlayerWHIP": ["whip"],
            "PlayerKs": ["ks"],
            "PlayerBB": ["players","bb", "walks"],
            "PlayerIP": ["ip"],
            "PlayerBAA": ["baa"],
            "PlayerFastballSpeed": ["fastball", "speed"],
            "PlayerArmVelo2": ["arm", "velo"],
            "PlayerChangeUpSpeed": ["change", "speed"],
            "PlayerPopTime": ["pop", "time"],
            "PlayerArmVelo3": ["arm", "velo"],
            "PlayerSB": ["sb"],
            "PlayerATT": ["attempts"],
            "CoachRecommend50": ["coach", "recommend", "50"],
            "PlayerRankingEstimate": ["where", "rank"],
            "PlayerAccomplishments": ["accomplishments"],
            "PlayerQuote": ["quote"],
            "Top3Org": ["top", "3", "org"],
            "Else": ["what", "else"],
            "Parent1Name": ["parent", "1", "name"],
            "Parent1Email": ["parent", "1", "email"],
            "Parent1Phone": ["parent", "1", "phone"],
            "Parent2Name": ["parent", "2", "name"],
            "Parent2Email": ["parent", "2", "email"],
            "Parent2Phone": ["parent", "2", "phone"],
            "Headshot": ["headshot", "photo"],
            "ContactFirstName": ["contact", "name", "first"],
            "ContactLastName": ["contact", "name", "last"],
            "ContactEmail": ["contact", "email"],
            "ContactPhone": ["contact", "phone"],
            "NominatorName": ["nominator", "name"],
            "NaminatorNameLast": ["nominator", "name", "last"],
            "NominatorEmail": ["nominator", "email"],
            "NominatorPhone": ["nominator", "phone"],
            "CoachNameFirst": ["coach", "name", "first"],
            "CoachNameLast": ["coach", "name", "last"],
            "CoachEmail": ["coach", "email"],
            "CoachPhone": ["coach", "phone"],
            "AthleteTeamPage": ["athlete", "team", "page"],
            "OrgLeader": ["org", "leader"],
            "OrgEmail": ["org", "email"],
            "OrgPhone": ["org", "phone"],
        }

        for standard_key, keywords in keyword_mappings.items():
            if all(keyword in column_name.lower() for keyword in keywords):
                return standard_key
        return column_name

    def make_players(self):
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
