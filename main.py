# Marking the board
from player import Player
from Board import Board

class Game(Board):
    def __init__(self, computer):
        super().__init__()
        self.computer = computer
        self.player = Player(super())


    def get_user_input(self):
        new_data =self.player.get_user_input(super())
        super().update(new_data, 'x')

    # Printing the board
    def display(self):
        data = super().get_data()
        p=1
        for _ in range(3):
            for _ in range(3):
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
