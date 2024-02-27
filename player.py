from error import newError

class Player():
    def __init__(self):
        self.player='x'
        
    def get_user_input(self, board):
        row = input("Enter row: ")
        column = input("Enter column: ")
        try:
            row = int(row)
            column = int(column)
            if row not in range(1, 4) or column not in range(1, 4):
                raise newError("Invalid input")
            if board[row-1][column-1] in ["X", "O"]:
                raise newError("Position taken")
            return row, column
        except (TypeError, ValueError) as e:
            raise newError("Invalid input") from e
        except newError as e:
            print(e)
            return self.get_user_input(board)
