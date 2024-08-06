import pandas as pd
from player import Player


class ExcelData:
    def __init__(self, file):
        self.file = file
        self.players = []
        self.attr_names = []

    def map_column(self, column_name):
        keyword_mappings = {
            "PlayerFirstName": [r"\bname\b", r"\bfirst\b", r"\bplayer\b"],
            "PlayerLastName": [r"\bname\b", r"\blast\b", r"\bplayer\b"],
            "Notes": [r"\bnotes\b"],
            "PlayerPosition": [r"\bprimary\b", r"\bposition\b"],
            "ClubTeamName": [r"\bteam\b", r"\bname\b"],
            "GameChangerName": [r"\bgame\b", r"\bchanger\b"],
            "PlayerPreviousRanked": [r"\bpreviously\b", r"\branked\b"],
            "PlayerRanking": [r"\branking\b"],
            "PlayerHometown": [r"\bhometown\b"],
            "HighSchoolName": [r"\bhigh\b", r"\bschool\b", r"\bhs\b"],
            "PlayerTwitter": [r"\btwitter\b"],
            "PlayerGPA": [r"\bgpa\b"],
            "PlayerRegion": [r"\bregion\b"],
            "PlayerCommitted": [r"\bcommitted\b"],
            "PlayerUniversity": [r"\buniversity\b"],
            "ActionVideo": [r"\baction\b", r"\bvideo\b"],
            "Slapper": [r"\bslapper\b"],
            "PlayerPA": [r"\bpa\b"],
            "PlayerAB": [r"\bat\b", r"\bbats\b", r"\bab\b"],
            "PlayerBA": [r"\bbatting\b", r"\bavg\b"],
            "PlayerOBP": [r"\bobp\b"],
            "PlayerOPS": [r"\bops\b"],
            "PlayerHits": [r"\bhits\b"],
            "PlayerDoubles": [r"\bdoubles\b"],
            "PlayerTriples": [r"\btriples\b"],
            "PlayerHR": [r"\bhomeruns\b", r"\bhr\b"],
            "PlayerRBI": [r"\brbi\b"],
            "PlayerStrikeOuts": [r"\bstrikeouts\b"],
            "FieldingPerc": [r"\bfielding\b", r"\b%\b"],
            "TotalChances": [r"\btcs\b"],
            "Assist": [r"\bassists\b"],
            "Putouts": [r"\bpos\b"],
            "PlayerArmVelo": [r"\barm\b", r"\bvelo\b"],
            "PlayerERA": [r"\bera\b"],
            "PlayerWHIP": [r"\bwhip\b"],
            "PlayerKs": [r"\bks\b"],
            "PlayerBB": [r"\bbb\b", r"\bwalks\b"],
            "PlayerIP": [r"\bip\b"],
            "PlayerBAA": [r"\bbaa\b"],
            "PlayerFastballSpeed": [r"\bfastball\b", r"\bspeed\b"],
            "PlayerArmVelo2": [r"\barm\b", r"\bvelo\b"],
            "PlayerChangeUpSpeed": [r"\bchange\b", r"\bspeed\b"],
            "PlayerPopTime": [r"\bpop\b", r"\btime\b"],
            "PlayerArmVelo3": [r"\barm\b", r"\bvelo\b"],
            "PlayerSB": [r"\bsb\b"],
            "PlayerATT": [r"\battempts\b"],
            "CoachRecommend50": [r"\bcoach\b", r"\brecommend\b", r"\b50\b"],
            "PlayerRankingEstimate": [r"\bwhere\b", r"\brank\b"],
            "PlayerAccomplishments": [r"\baccomplishments\b"],
            "PlayerQuote": [r"\bquote\b"],
            "Top3Org": [r"\btop\b", r"\b3\b", r"\borg\b"],
            "Else": [r"\bwhat\b", r"\belse\b"],
            "Parent1Name": [r"\bparent\b", r"\b1\b", r"\bname\b"],
            "Parent1Email": [r"\bparent\b", r"\b1\b", r"\bemail\b"],
            "Parent1Phone": [r"\bparent\b", r"\b1\b", r"\bphone\b"],
            "Parent2Name": [r"\bparent\b", r"\b2\b", r"\bname\b"],
            "Parent2Email": [r"\bparent\b", r"\b2\b", r"\bemail\b"],
            "Parent2Phone": [r"\bparent\b", r"\b2\b", r"\bphone\b"],
            "Headshot": [r"\bheadshot\b", r"\bphoto\b"],
            "ContactFirstName": [r"\bcontact\b", r"\bname\b", r"\bfirst\b"],
            "ContactLastName": [r"\bcontact\b", r"\bname\b", r"\blast\b"],
            "ContactEmail": [r"\bcontact\b", r"\bemail\b"],
            "ContactPhone": [r"\bcontact\b", r"\bphone\b"],
            "NominatorName": [r"\bnominator\b", r"\bname\b"],
            "NaminatorNameLast": [r"\bnominator\b", r"\bname\b", r"\blast\b"],
            "NominatorEmail": [r"\bnominator\b", r"\bemail\b"],
            "NominatorPhone": [r"\bnominator\b", r"\bphone\b"],
            "CoachNameFirst": [r"\bcoach\b", r"\bname\b", r"\bfirst\b"],
            "CoachNameLast": [r"\bcoach\b", r"\bname\b", r"\blast\b"],
            "CoachEmail": [r"\bcoach\b", r"\bemail\b"],
            "CoachPhone": [r"\bcoach\b", r"\bphone\b"],
            "AthleteTeamPage": [r"\bathlete\b", r"\bteam\b", r"\bpage\b"],
            "OrgLeader": [r"\borg\b", r"\bleader\b"],
            "OrgEmail": [r"\borg\b", r"\bemail\b"],
            "OrgPhone": [r"\borg\b", r"\bphone\b"],
        }

        # Normalize the column name by removing spaces and converting to lowercase
        normalized_column_name = ''.join(column_name.lower().split())

        for standard_key, keywords in keyword_mappings.items():
            # Calculate the number of keywords present
            keyword_count = sum(keyword in normalized_column_name for keyword in keywords)
            # Check if more than half of the keywords are present
            if keyword_count / len(keywords) > 0.5:
                return standard_key
        return column_name

    def make_players(self):
        try:
            df = pd.read_excel(self.file)
            df.rename(columns=lambda x: self.map_column(x.strip()), inplace=True)
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
