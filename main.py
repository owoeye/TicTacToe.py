from engine import Board
from scores import Score
from player import Player

# set board locations
board = Board()

# create img of board
board.load_board()

# player selects X or O
gamer = Player()
gamer.player_select()
# print(gamer.players)

score = Score()
while True:

    for user in ["x", "o"]:
        # Enter location you want to play
        while True:
            row = 0
            col = 0
            while True:
                try:
                    col = int(input(f"player{gamer.players.index(user) + 1} enter column you want to play: ")) - 1
                    row = int(input(f"player{gamer.players.index(user) + 1} enter row you want to play: ")) - 1
                except ValueError:
                    print("invalid row or col")
                    continue
                else:
                    break

            # check if the  move is valid
            # edit board locations amd input move for player
            if board.update_board(user, row, col):
                break

        board.load_board()

        # check for winner
        if board.check_for_winner():
            print(f"player{gamer.players.index(user) + 1} wins")
            score.update_score(gamer.players.index(user))
            print(f"Score: {score.score_board[0]} - {score.score_board[1]}")

            board.board_reset()
            break

        # check for tie
        elif board.check_for_tie():
            print("It's a tie")
            print(f"Score: {score.score_board[0]} - {score.score_board[1]}")

            board.board_reset()
            break



