from error import newError


class Board:
    def __init__(self):
        self.board=[[" " for _ in range(3)] for _ in range(3)]
        self.set_empty()

    def set_empty(self):  # sourcery skip: use-itertools-product
      for row in self.board:
          for index in row:
              index = " "

    def update(self, row,column, player):
        self.board[row-1][column-1] = player

    def get_data(self):
        return self.board

    def checkPosition(self, row, column):
        if self.board[userInput] in ["X", "O"]:
            raise newError("Position taken")
    def display(self):
        for row in self.board:
            column = iter(row)
            print(next(column), "|", next(column), "|", next(column))
            
if __name__ == "__main__":
    board = Board()
    board.set_empty()
    board.display()
    print()
    board.update(1,1, "x")
    board.display()
