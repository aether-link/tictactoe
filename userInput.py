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
                self.checkPosition(self)
                raise rangeError

        except ValueError:
            print("Invalid input")
            self.get_user_input(self)
        except rangeError:
            print("Out of range, Enter between 1 and 9")
            self.get_user_input(self)
        except nonEmptyError:
            print("Position already filled, \n\t Try Again")
            self.get_user_input(self)

    def checkPosition(self, Position):
        if not Position:
            Position = self.userInput
        if self.human[Position] | self.computer[Position]:
            raise nonEmptyError
