# Marking the board
from player import Player
from Board import Board

class Game(Board):
    def __init__(self):
        self.board = Board()
        self.player = Player(self.board.get_data())

    def get_user_input(self):
        new_data =self.player.get_user_input(self.board)
        self.board.update(new_data, 'x')

    # Printing the board
    def display(self):
        data = self.board.get_data()
        p=1
        for j in range(0, 3):
            for i in range(0, 3):
                print('|', end='')
                if(data[p]!=" "):
                    print(f' {data[p]} ', end='')
                else:
                    print("   ", end='')
                p+=1
            print('|')


if __name__ == '__main__':
    # Dictionary to store the board records
    
    
    game = Game()
    game.display()
    game.get_user_input()
    game.display()
    #end
