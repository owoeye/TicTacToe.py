class Board:

    def __init__(self):
        self.board_locations = [["   ", "   ", "   "],
                                ["   ", "   ", "   "],
                                ["   ", "   ", "   "]]

    def load_board(self):
        board = f"{'|'.join(self.board_locations[0])}\n" \
                "-----------\n" \
                f"{'|'.join(self.board_locations[1])}\n" \
                "-----------\n" \
                f"{'|'.join(self.board_locations[2])}"
        print(board)

    def check_for_tie(self):
        for move in self.board_locations:
            return not ("   " in move)

    def check_for_winner(self):
        return self.board_locations[0][0] == self.board_locations[0][1] == self.board_locations[0][2] != "   " \
               or self.board_locations[1][0] == self.board_locations[1][1] == self.board_locations[1][2] != "   " \
               or self.board_locations[2][0] == self.board_locations[2][1] == self.board_locations[2][2] != "   " \
               or self.board_locations[0][0] == self.board_locations[1][1] == self.board_locations[2][2] != "   " \
               or self.board_locations[0][2] == self.board_locations[1][1] == self.board_locations[2][0] != "   " \
               or self.board_locations[0][0] == self.board_locations[1][0] == self.board_locations[2][0] != "   " \
               or self.board_locations[0][1] == self.board_locations[1][1] == self.board_locations[2][1] != "   " \
               or self.board_locations[0][2] == self.board_locations[1][2] == self.board_locations[2][2] != "   "

    def update_board(self, player, row, col):
        if (col or row) > 3:
            print("invalid input")
        elif self.board_locations[row][col] != "   ":
            print(f"'{self.board_locations[row][col]}' is already played in this location")
            print("Play elsewhere!!!")
        else:
            self.board_locations[row][col] = f" {player.upper()} "
            return True

    def board_reset(self):
        self.board_locations = [["   ", "   ", "   "],
                                ["   ", "   ", "   "],
                                ["   ", "   ", "   "]]
        self.load_board()
