from decimal import Decimal, ROUND_HALF_UP
import re


class Player:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])

    def __str__(self):
        return self.__repr__()

    def calculate_player_score(self, player):
        infield_stats = 0
        batting_stats = 0
        if player.PlayerPosition == "Pitcher":
            return 0
        elif player.PlayerPosition == "Catcher":
            return 0
        else:
            infield_stats = sum(
                [
                    getattr(player, arg, 0)
                    for arg in ["TotalChances", "Assists", "Putouts", "FieldingPerc"]
                    if isinstance(getattr(player, arg, 0), (int, float))
                ]
            )

        batting_stats = sum(
            [
                getattr(player, arg, 0)
                for arg in ["OBP", "OPS", "QAB"]
                if isinstance(getattr(player, arg, 0), (int, float))
            ]
        )
        return infield_stats, batting_stats
