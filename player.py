class newError(Exception):
    pass

class Player:
    def __init__(self, computer):
        self.human= {
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
        self.computer = computer
        self.userInput = None
    def get_positions(self):
        return self.human

    def get_user_input(self):
        self.userInput = input("Enter your move:")
        try:
            self.userInput = int(self.userInput)
            if self.userInput < 1 or self.userInput > 9:
                raise newError("Value out of range")
            else:
                self.checkPosition()
                self.update()

        except ValueError:
            print("Invalid input")
            self.get_user_input()

        except newError as e:
            print(e)
            self.get_user_input()
              
    def update(self):
        self.human[self.userInput]=True
    def checkPosition(self):
        if self.human[self.userInput]==True or self.computer[self.userInput]==True:
            raise newError("Position taken")
        
