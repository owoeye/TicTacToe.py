class Score:
    def __init__(self):
        self.scoreX = 0
        self.scoreO = 0
        self.score_board = [self.scoreX, self.scoreO]

    def update_score(self, index):
        self.score_board[index] += 1
