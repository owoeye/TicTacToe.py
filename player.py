class Player:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.players = [self.player1, self.player2]

    def player_select(self):
        invalid = True
        while invalid:
            self.players[0] = input("player1 select X or O: ").lower()
            # if first == "x":
            #     self.players[0] = first
            # elif first == "o":
            #     self.players[1] = first

            if self.players[0] == "x":
                self.players[1] = "o"
                print("player2 is 'O'")
                print("player1 plays first")
                invalid = False
            elif self.players[0] == "o":
                self.players[1] = "x"
                # self.players[1] = "o"
                print("player2 is 'X")
                print("player2 plays first")
                invalid = False
            else:
                print("invalid input")

