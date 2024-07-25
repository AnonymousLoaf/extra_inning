from decimal import Decimal, ROUND_HALF_UP
import re


class Player:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])

    def __str__(self):
        return self.__repr__()

    def calculate_player_score(self):
        infield_stats = 0
        batting_stats = 0
        return infield_stats, batting_stats
