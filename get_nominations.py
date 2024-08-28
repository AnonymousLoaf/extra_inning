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
            "LastYearRank": [r"\blast\b", r"\byear\b", r"\branked\b", r"\bwhere\b"],
            "RankedThisYear": [r"\branked\b", r"\bthis\b", r"\byear\b"],
            "WhereToRankRegionallyCoach": [r"\bregionally", r"\brank\b", r"\bcoach\b"],
            "WhereToRankNationallyCoach": [r"\bnationally\b", r"\brank\b", r"\bcoach\b"],
            "PrefferedRecomendation": [r"\bpreferred\b", r"\brecommendations\b"],
            "Done": [r"\bdone\b"],
            "Notes": [r"\bnotes\b"],
            "PlayerFirstName": [r"\bname\b", r"\bfirst\b", r"\bplayer\b"],
            "PlayerLastName": [r"\bname\b", r"\blast\b", r"\bplayer\b"],
            "RankedPrevious": [r"\blast\b", r"\branked\b", r"\byear\b"],
            "PlayerHometown": [r"\bhometown\b"],
            "PlayerHighSchool": [r"\bhigh\b", r"\bschool\b"],
            "x": [r"\bx\b"],
            "PlayerGPA": [r"\bgpa\b"],
            "PlayerRegion": [r"\bregion\b"],
            "PlayerCommitted": [r"\bcommitted\b"],
            "PlayerUniversity": [r"\buniversity\b"],
            "ActionVideo": [r"\baction\b", r"\bvideo\b"],
            # Hitting stats
            "Slapper": [r"\bslapper\b"],
            "PlayerPA": [r"\bplate\b", r"\bappearances\b"],
            "PlayerAB": [r"\bat\b", r"\bbats\b"],
            "PlayerBA": [r"\bba\b"],
            "PlayerOBP": [r"\bobp\b"],
            "PlayerOPS": [r"\bops\b"],
            "PlayerHits": [r"\bhits\b"],
            "PlayerDoubles": [r"\bdoubles\b"],
            "PlayerTriples": [r"\btriples\b"],
            "PlayerHR": [r"\bhomeruns\b"],
            "PlayerRBI": [r"\brbis\b"],
            "PlayerStrikeOuts": [r"\bkk\b"],
            "PlayerPosition": [r"\bprimary\b", r"\bposition\b"],
            "FieldingPerc": [r"\bfielding\b"],
            "TotalChances": [r"\btcs\b"],
            "Assist": [r"\bassists\b"],
            "Putouts": [r"\bpos\b"],
            "PlayerArmVelo": [r"\barm\b", r"\bvelo\b"],
            # Pitcher stats
            "PlayerERA": [r"\bera\b"],
            "PlayerWHIP": [r"\bwhip\b"],
            "PlayerKs": [r"\bks\b"],
            "PlayerBB": [r"\bbb\b", r"\bwalks\b"],
            "PlayerIP": [r"\binnings\b", r"\bpitched\b"],
            "PlayerBAA": [r"\bbaa\b"],
            "PlayerFastballSpeed": [r"\bfastball\b", r"\bspeed\b"],
            "PlayerChangeUpSpeed": [r"\bchange\b", r"\bspeed\b"],
            # Catcher stats
            "PlayerPopTime": [r"\bpop-time\b"],
            "PlayerSB": [r"\bsb\b"],
            "PlayerATT": [r"\battempts\b"],
            "PlayerAccomplishments": [r"\baccomplishments\b"],
            "CoachQuote": [r"\bquote\b", r"\bcoach\b"],
            "PlayersRecOutsideOrg": [r"\bplayers\b", r"\boutside\b", r"\borganization\b"],
            "TopTournaments": [r"\btop\b", r"\btournaments\b"],
            "WhatElse": [r"\bwhat\b", r"\belse\b"],
            "ParentFirstName": [r"\bparent\b", r"\bfirst\b", r"\bname\b"],
            "ParentLastName": [r"\bparent\b", r"\blast\b", r"\bname\b"],
            "ParentEmail": [r"\bparent\b", r"\bemail\b"],
            "ParentPhone": [r"\bparent\b", r"\bphone\b"],
            "Headshot": [r"\bheadshot\b", r"\bphoto\b"],
            "ContactFirstName": [r"\bcontact\b", r"\bname\b", r"\bfirst\b"],
            "ContactLastName": [r"\bcontact\b", r"\bname\b", r"\blast\b"],
            "ContactEmail": [r"\bcontact\b", r"\bemail\b"],
            "ContactPhone": [r"\bcontact\b", r"\bphone\b"],
            "NominatorFirstName": [r"\bnominator\b", r"\bname\b", r"\bfirst\b"],
            "NominatorLastName": [r"\bnominator\b", r"\bname\b", r"\blast\b"],
            "NominatorEmail": [r"\bnominator\b", r"\bemail\b"],
            "NominatorPhone": [r"\bnominator\b", r"\bphone\b"],
            "CoachNameFirst": [r"\bcoach\b", r"\bname\b", r"\bfirst\b"],
            "CoachNameLast": [r"\bcoach\b", r"\bname\b", r"\blast\b"],
            "CoachEmail": [r"\bcoach\b", r"\bemail\b"],
            "CoachPhone": [r"\bcoach\b", r"\bphone\b"],
            "ClubTeamName": [r"\bteam\b", r"\bname\b"],
            "GameChangerName": [r"\bgame\b", r"\bchanger\b"],
            "AthletesGoLiveName": [r"\bathletes\b", r"\bgo\b", r"\blive\b"],
            "OrgLeaderFirstName": [r"\borg\b", r"\bleader\b", r"\bfirst\b", r"\bname\b"],
            "OrgLeaderLastName": [r"\borg\b", r"\bleader\b", r"\blast\b", r"\bname\b"],
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
            "PlayerHits": (15, None),
            "PlayerPA": (40, None),
            "PlayerRBI": (8, None),
            "PlayerERA": (None, 3.2),
            "PlayerIP": (50, None),
            "FieldingPerc": (0.900, 1),
            "PlayerArmVelo": (0, None),
        }

        for player in self.players:
            for stat, (min_val, max_val) in gen_threshold.items():
                try:
                    stat_value = getattr(player, stat)
                    if stat_value is not None:
                        # Attempt to convert stat_value to a float for comparison
                        try:
                            stat_value = float(stat_value)
                        except ValueError:
                            continue  # Skip if stat_value cannot be converted to a float
                        
                        if min_val is not None and stat_value < min_val:
                            player.is_red_flag.append(stat)
                        if max_val is not None and stat_value > max_val:
                            player.is_red_flag.append(stat)
                except AttributeError:
                    pass




    def get(self, name):
        for player in self.players:
            full_name = player.PlayerFirstName + " " + player.PlayerLastName
            if full_name == name:
                return player
        return None
