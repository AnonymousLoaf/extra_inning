from scoring import (
    player_defense_score,
    player_pitching_score,
    player_catching_score,
    player_batting_score,
    player_num_national_tournaments
)


class Player:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.pos_batting_rank = None
        self.global_batting_rank = None
        self.pitching_score = 0
        self.catching_score = 0
        self.defensive_score = 0
        self.batting_score = 0
        self.catcher_score = 0
        self.infield_score = 0
        self.outfield_score = 0
        self.is_red_flag = []
        self.error_list = []
        self.num_national_tournament = 0
        self.CalculatedFieldingPerc = 0
        self.CalculatedBA = 0


    def __repr__(self):
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])

    def __str__(self):
        return self.__repr__()

    def calculate_player_score(self):
        self.pitching_score = player_pitching_score(self, self.error_list)
        self.catching_score = player_catching_score(self, self.error_list)
        self.defensive_score = player_defense_score(self, self.error_list)
        self.batting_score = player_batting_score(self, self.error_list)
        self.num_national_tournament = player_num_national_tournaments(self, self.error_list)
        self.pitcher_score = (self.pitching_score * 1)
        self.catcher_score = (self.catching_score * 0.6) + (self.batting_score * 0.4)
        self.infield_score = (self.defensive_score * 0.6) + (self.batting_score * 0.4)
        self.outfield_score = (self.defensive_score * 0.40) + (self.batting_score * 0.60)
