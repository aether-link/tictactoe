# Marking the board
from player import Player
from Board import Board

class Game(Board):
    def __init__(self, computer):
        self.board = Board()
        self.computer = computer
        self.data = self.board.get_data()
        self.player = Player(self.data)

    def get_user_input(self):
        new_data =self.player.get_user_input(self.board)
        self.board.update(new_data, 'x')
        self.data = self.board.get_data()

    # Printing the board
    def display(self):
        p=1
        for j in range(0, 3):
            for i in range(0, 3):
                print('|', end='')
                if(self.data[p]!=" "):
                    print(f' {self.data[p]} ', end='')
                else:
                    print("   ", end='')
                p+=1
            print('|')


if __name__ == '__main__':
    # Dictionary to store the board records
    
    computer={
        1: False,
        2: True,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        }
    game = Game(computer)
    game.display()
    game.get_user_input()
    game.display()
    #end
