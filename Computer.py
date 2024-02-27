from Board import Board


class Computer(Board):
    def __init__(self, board):
        self.player = "O"
        self.data = board

    # from Board import Board


class Computer:
    def __init__(self, board):
        self.player = "O"
        self.data = board

    def calculate(self):
        user_move = []
        computer_move = []
        empty = []
        for i in range(1, 10):
            if self.data[i] == "X":
                user_move.append(i - 1)
            elif self.data[i] == self.player:
                computer_move.append(i - 1)
            else:
                empty.append(i - 1)
        print(f"{user_move} com: {computer_move} emp: {empty}")


if __name__ == "__main__":
    board = {
        1: " ",
        2: " ",
        3: " ",
        4: " ",
        5: " ",
        6: "O",
        7: " ",
        8: " ",
        9: " ",
    }
    computer = Computer(board)
    computer.calculate()
