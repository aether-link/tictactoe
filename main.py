# Marking the board
from userInput import Player

def mark(h,c):
    if(h | c):
        if(h):
            print(' O ', end='')
        else:
            print(' X ', end='')
    else:
        print('   ', end='')

# Printing the board
def display(human, computer):
    p=1
    for j in range(0, 3):
        for i in range(0, 3):
            print('|', end='')
            mark(human[p], computer[p])
            p+=1
        print('|')


if __name__ == '__main__':
    # Dictionary to store the board records
    human = {
        1: True,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
    }
    computer = {
        1: False,
        2: False,
        3: True,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,

    }
    display(human, computer)
    p1 = Player(human,computer)
    p1.get_user_input()