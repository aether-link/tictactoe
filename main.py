# Marking the board
from player import Player
from Board import Board

winning_conditions = [
    [(0, 0), (0, 1), (0, 2)],  # row 1
    [(1, 0), (1, 1), (1, 2)],  # row 2
    [(2, 0), (2, 1), (2, 2)],  # row 3
    [(0, 0), (1, 0), (2, 0)],  # column 1
    [(0, 1), (1, 1), (2, 1)],  # column 2
    [(0, 2), (1, 2), (2, 2)],  # column 3
    [(0, 0), (1, 1), (2, 2)],  # diagonal 1
    [(0, 2), (1, 1), (2, 0)],  # diagonal 2
]

class Game(Board):
    def __init__(self):
        super().__init__()
        self.player = Player()


    def get_user_input(self):
        row, column = self.player.get_user_input(board=super().get_data())
        super().update(row, column, self.player.player)

    # Printing the board
    def display(self):
        super().display()
        
    def reset(self):
        super().set_empty()
        

    def check_winner(self):
        pass

if __name__ == '__main__':
    game = Game()
    
    GameOver = False
    while(not GameOver):
        game.reset()
        