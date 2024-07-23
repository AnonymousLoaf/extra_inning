from decimal import Decimal, ROUND_HALF_UP
import re


class Player:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])

    def __str__(self):
        return self.__repr__()

    def calculate_player_score(player):
        if player.PlayerPosition == "Pitcher":
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
            return infield_stats + batting_stats

    def clean(self):
        for key, value in self.__dict__.items():
            percentages = ["OBP", "OPS", "QAB", "FieldingPerc"]
            number = [
                "TotalChances",
                "Assists",
                "Putouts",
                "ERA",
                "BAA",
                "FBandCU",
                "KBB",
                "PopTime",
            ]
            if key in percentages:
                pattern = r"\b(\d+\.\d+)\b"
                matches = re.findall(pattern, value)
                if matches:
                    decimal_matches = [Decimal(match) for match in matches]
                    avg = sum(decimal_matches) / Decimal(len(decimal_matches))
                    avg_rounded = avg.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
                    avg_float = float(avg_rounded)
                    setattr(self, key, avg_float)
            elif key in number:
                pattern = r"\b(\d+)\b"
                matches = re.findall(pattern, value)
                if matches:
                    setattr(self, key, int(matches[0]))
