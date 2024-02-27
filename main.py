# Marking the board
from player import Player
from Board import Board

winning_conditions = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
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

    def check_winner(self):
        pass

if __name__ == '__main__':
    # Dictionary to store the board records
    
    
    game = Game()
    game.display()
    game.get_user_input()
    game.display()
    #end
