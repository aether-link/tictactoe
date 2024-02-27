from Board import Board
from error import newError

class Player(Board):
    def __init__(self, board_data):
        self.board_data=board_data
        self.player='x'
        
    def get_user_input(self, board):
        userInput = input("Enter your move:")
        try:
            userInput = int(userInput)
            if userInput < 1 or userInput > 9:
                raise newError("Value out of range")
            board.checkPosition(userInput)

            return userInput

        except ValueError:
            print("Invalid input")
            self.get_user_input(board)

        except newError as e:
            print(e)
            self.get_user_input(board)
              
    

