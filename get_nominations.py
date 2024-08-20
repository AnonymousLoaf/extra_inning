import pandas as pd
from player import Player
import re


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
            "PlayerAB": [r"\bat\b", r"\bbats\b"],
            "PlayerBA": [r"\bbatting\b", r"\bavg\b"],
            "PlayerOBP": [r"\bobp\b"],
            "PlayerOPS": [r"\bops\b"],
            "PlayerHits": [r"\bhits\b"],
            "PlayerDoubles": [r"\bdoubles\b"],
            "PlayerTriples": [r"\btriples\b"],
            "PlayerHR": [r"\bhomeruns\b"],
            "PlayerRBI": [r"\brbi\b"],
            "PlayerStrikeOuts": [r"\bstrikeouts\b"],
            "FieldingPerc": [r"\bfielding\b"],
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
            "PlayerChangeUpSpeed": [r"\bchange\b", r"\bspeed\b"],
            "PlayerPopTime": [r"\bpop-time\b"],
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

        for standard_key, patterns in keyword_mappings.items():
            # Check if all patterns in the set match the column name
            if all(re.search(pattern, column_name, re.IGNORECASE) for pattern in patterns):
                return standard_key
        # If no patterns match, return the original column name
        return column_name

    def make_players(self):
        try:
            df = pd.read_excel(self.file)

            # Start merging process directly here
            reverse_map = {}
            for col in df.columns:
                mapped_col = self.map_column(col.strip())
                if mapped_col in reverse_map:
                    reverse_map[mapped_col].append(col)
                else:
                    reverse_map[mapped_col] = [col]

            # Merge columns by combining them without overwriting non-NaN values
            for key, cols in reverse_map.items():
                if len(cols) > 1:
                    # Use the first column as the base and update with non-NaN values from other columns
                    merged_col = df[cols[0]]
                    for col in cols[1:]:
                        merged_col = merged_col.fillna(df[col])
                    df[key] = merged_col
                    # Drop the original columns after merging
                    df.drop(columns=cols, inplace=True)
                else:
                    # Rename the single column directly
                    df.rename(columns={cols[0]: key}, inplace=True)

            self.attr_names = df.columns.tolist()
            for _, row in df.iterrows():
                self.players.append(Player(**row.to_dict()))
        except FileNotFoundError:
            print(f"File '{self.file}' not found.")
        except Exception as e:
            print(f"Error loading players: {e}")


    def check_players(self):
        gen_threshold = {
            "PlayerBA": (0.25, 1),
            "PlayerOPS": (0.7, None),
            "PlayerOBP": (0.3, 1),
            "PlayerAB": (50, None),
            "PlayerStrikeOuts": (0, None),
            "PlayerHits": (30, None),
            "PlayerPA": (75, None),
            "PlayerRBI": (8, None),
            "PlayerERA": (None, 3.2),
            "PlayerIP": (50, None),
            "FieldingPerc": (0.955, 1),
            "PlayerArmVelo": (0, None),
        }

        for player in self.players:
            for stat, (min_val, max_val) in gen_threshold.items():
                stat_value = getattr(player, stat)
                if (min_val is not None and stat_value < min_val) or (max_val is not None and stat_value > max_val):
                    player.is_red_flag.append(stat)


    def get(self, name):
        for player in self.players:
            full_name = player.PlayerFirstName + " " + player.PlayerLastName
            if full_name == name:
                return player
        return None
