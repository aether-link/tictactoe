from error import newError


class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.set_empty()

    def set_empty(self):
        for row in range(3):
            for column in range(3):
                self.board[row][column] = " "

    def update(self, row, column, player):
        self.board[row][column] = player
        self.display()

    def get_data(self):
        return self.board

    def checkPosition(self, row, column, player="X", computer="O"):
        return self.board[row-1][column-1] not in [player, computer]

    def display(self):
        for row in self.board:
            column = iter(row)
            print("|", next(column), "|", next(column), "|", next(column), "|")


if __name__ == "__main__":
    board = Board()
    board.set_empty()
    board.display()
    print()
    board.update(1, 1, "X")
    board.display()
    print(board.checkPosition(1,1))
