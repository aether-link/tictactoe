from error import newError


class Player:
    def __init__(self, player="X", computer="O"):
        self.player = player
        self.computer = computer

    def get_user_input(self, board):
        while True:
            row = input("Enter row: ")
            column = input("Enter column: ")
            if row.isdigit() & column.isdigit():
                return int(row), int(column)
            else:
                print("Invalid Input, Try Again!")
