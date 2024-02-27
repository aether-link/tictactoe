from error import newError
class Board:
    def __init__(self):
        self.board = {}
        self.set_empty()
        
    def set_empty(self):
        self.board = {
        1: " ",
        2: " ",
        3: " ",
        4: " ",
        5: " ",
        6: " ",
        7: " ",
        8: " ",
        9: " ",
        }
    
    def update(self,userInput,player):
        self.board[userInput] = "x"
    
    def get_data(self):
        return dict(self.board)
    
    def checkPosition(self, userInput):
        if self.board[userInput] in ['X', 'O']:
            raise newError("Position taken")
    