from player import Player
import csv

class CSVData:
    def __init__(self, file):
        self.file = file
        self.players = []
        self.attr_names = []

    def load_players(self):
        try:
            with open(self.file, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.players.append(Player(**row))
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
            if player.PlayerName == name:
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
        "What organization does this player play in?": "PlayerOrganization",
        "Organization Point of Contact Name": "OrganizationContactName",
        "Organization Point of Contact Phone Number": "OrganizationContactPhone",
        "Game Changer Team Name": "GameChangerTeamName",
        "Primary Position of Player": "PlayerPosition",
        "High School Name": "HighSchoolName",
        "What is this player's BA average over the last 12 months? [required]" : "PlayerBA",
        "What is this player's OBP average over the last 12 months? [required]" : "PlayerOBP",
        "What is this player's OPS average over the last 12 months? [required]" : "PlayerOPS",
        "What is this player's QAB% average over the last 12 months? [required]" : "PlayerQAB",
        "What is this player's fielding % average over the last 12 months? [required]": "FieldingPerc",
        "What is this player's arm velo?" : "ArmVelo",
        "What is this player's TCs % average over the last 12 months? [required]" : "TotalChances",
        "Average for Assists (total / innings played over last 12 months?" : "Assists",
        "Average POs (total / innings played over the last 12 months?" : "Putouts",
        "What is this players ERA over the last 12 months?" : "PlayerERA",
        "What is this players WHIP over the last 12 months?" : "PlayerWHIP",
        "What is this players Ks over the last 12 months?" : "PlayerKs",
        "What is this players BB (walks) over the last 12 months?" : "PlayerBB",
        "What is this players IP (innings pitched) over the last 12 months?" : "PlayerIP",
        "What is this players BAA over the last 12 months?" : "PlayerBAA",
        "What is this pitchers fastball speed?" : "PlayerFastballSpeed",
        "What is this pitchers change-up speed?" : "PlayerChangeUpSpeed",
        "What is this player's pop-time?" : "PlayerPopTime",
        "Where do you think this player should be ranked nationally?" : "PlayerRankingEstimate",
        "Why should this player be ranked here?" : "PlayerRankingReason",
        "Share this players individual accomplishments (List in bulleted format)": "PlayerAccomplishments",
        "Events this player participate in over the last 12 months? (list in bulleted format)": "PlayerEvents",
        "Name at least 3 quality teams this player faced over the last 12 months": "PlayerQualityTeams",
        "Which Region does this player live in?": "PlayerRegion",
        "Player Facebook  (Example: Extra Inning Softball)": "PlayerFacebook",
        "Player Instagram Handle (Example: extrainningsoftball)": "PlayerInstagram",
        "Player X - Twitter Handle (Example: @ExtraInningSB)": "PlayerTwitter",
        "Parent(s) or Guardian Name": "ParentName",
        "Parent(s) or Guardian Email": "ParentEmail",
        "Parent(s) or Guardian Phone Number": "ParentPhone",
        "College committed to (if applicable)": "PlayerCollegeCommitted",
        "Secondary/Other Position(s) of Player: (Mark as N/A if not applicable)": "PlayerSecondaryPosition",
        "Player Hometown/State": "PlayerHometown",
        "Provide a quote from one of the player's coaches (may be published)": "PlayerQuote",
        "Human Interest Insights": "PlayerHumanInterest",
        "Recruiting news (if applicable)": "PlayerRecruitingNews",
        "Headshot": "PlayerHeadshot",
        "Action Photo": "PlayerActionPhoto",
    }