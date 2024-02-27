from error import newError


class Board:
    def __init__(self):
        self.board=[[" " for _ in range(3)] for _ in range(3)]
        self.set_empty()

    def set_empty(self):  # sourcery skip: use-itertools-product
      for row in self.board:
          for index in row:
              index = " "

    def update(self, userInput, player):
        self.board[userInput] = "x"

    def get_data(self):
        return dict(self.board)

    def checkPosition(self, userInput):
        if self.board[userInput] in ["X", "O"]:
            raise newError("Position taken")
    def display(self):
        for row in self.board:
            print(row)
            
board = Board()
board.set_empty()
board.display()
