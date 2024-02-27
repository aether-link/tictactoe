from Board import Board
import random




class Computer:
    def __init__(self):
        self.player = "O"

    def get_board_data(self, board):
        user_move = []
        computer_move = []
        empty = []
        data = board.get_data()
        for i in range(1, 10):
            if data[i] == "X":
                user_move.append(i - 1)
            elif data[i] == player:
                computer_move.append(i - 1)
            else:
                empty.append(i - 1)
        user_move.sort()
        computer_move.sort()
        empty.sort()
        print(f"{user_move} com: {computer_move} emp: {empty}")
        return {"user_move": user_move, "computer_move": computer_move, "empty": empty}

    def calculate(self, board):
        data = self.get_board_data(board)
        user_moves = data["user_move"]
        print(user_moves)



if __name__ == "__main__":
    computer = Computer()
    computer.calculate(board=board)
