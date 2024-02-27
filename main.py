# Marking the board
from player import Player
from Board import Board

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


if __name__ == '__main__':
    # Dictionary to store the board records
    
    
    game = Game()
    game.display()
    game.get_user_input()
    game.display()
    #end
