# Marking the board
from player import Player

class Game:
    def __init__(self, computer):
        
        self.computer = computer
        self.player = Player(computer)
        self.human= self.player.get_positions()

    def get_user_input(self):
        self.player.get_user_input()

    def mark(self,h,c):
        if(h | c):
            if(h):
                print(' O ', end='')
            else:
                print(' X ', end='')
        else:
            print('   ', end='')

    # Printing the board
    def display(self):
        p=1
        for j in range(0, 3):
            for i in range(0, 3):
                print('|', end='')
                self.mark(self.human[p], self.computer[p])
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
    game =Game( computer)
    game.display()
    game.get_user_input()
    game.display()