class ComparePlayer:
    def __init__(self):
        pass

    def get_score(self, player1, player2, *args):
        player1_score = sum([getattr(player1, arg) for arg in args if isinstance(getattr(player1, arg), (int, float))])
        player2_score = sum([getattr(player2, arg) for arg in args if isinstance(getattr(player2, arg), (int, float))])
        return player1_score, player2_score
