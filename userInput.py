class newError(Exception):
    pass

class Player:
    def __init__(self, human, computer):
        self.human = human
        self.computer = computer
        self.userInput = None

    def get_user_input(self):
        self.userInput = input("Enter your move:")
        try:
            self.userInput = int(self.userInput)
            if self.userInput < 1 or self.userInput > 9:
                raise newError("Value out of range")
            else:
                self.checkPosition()

        except ValueError:
            print("Invalid input")
            self.get_user_input()
        except newError as e:
            print(e)
            self.get_user_input()
        

    def checkPosition(self):
        if self.human[self.userInput]==True or self.computer[self.userInput]==True:
            raise newError("Position taken")
