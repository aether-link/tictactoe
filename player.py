class Player:
    def __init__(self, player="X", computer="O"):
        self.player = player
        self.computer = computer

    def get_user_input(self, board):
        while True:
            row = input("Enter row: ")
            column = input("Enter column: ")
            if row.isdigit() & column.isdigit():
                row, column = int(row), int(column)
                if row<=3 and column<=3:
                    return row, column
                else:
                    print("Value out of range, Try Again!")
            else:
                print("Invalid Input, Try Again!")
