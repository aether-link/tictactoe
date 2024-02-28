# Marking the board
from player import Player
from computer import Computer
from Board import Board

winning_conditions = [
    [(0, 0), (0, 1), (0, 2)],  # row 1
    [(1, 0), (1, 1), (1, 2)],  # row 2
    [(2, 0), (2, 1), (2, 2)],  # row 3
    [(0, 0), (1, 0), (2, 0)],  # column 1
    [(0, 1), (1, 1), (2, 1)],  # column 2
    [(0, 2), (1, 2), (2, 2)],  # column 3
    [(0, 0), (1, 1), (2, 2)],  # diagonal 1
    [(0, 2), (1, 1), (2, 0)],  # diagonal 2
]


class Game(Board, Player, Computer):
    def __init__(self, player="X", computer="O"):
        super().__init__()
        self.player = player
        self.computer = computer

    def get_moves(self, symbol):
        # sourcery skip: for-append-to-extend, inline-immediately-returned-variable, list-comprehension, use-itertools-product
        moves = []
        for row in range(3):
            for column in range(3):
                if super().get_data()[row][column] == symbol:
                    moves.append((row, column))
        return moves

    def get_available_moves(self):
        return self.get_moves(" ")

    def get_player_moves(self):
        return self.get_moves(self.player)

    def get_computer_moves(self):
        return self.get_moves(self.computer)

    # Printing the board
    def display(self):
        super().display()

    def reset(self):
        super().set_empty()

    def check_winner(self):
        if super().check(super().get_data(), self.player, winning_conditions):
            return self.player
        if super().check(super().get_data(), self.computer, winning_conditions):
            return self.computer

    def get_player_input(self):
        row, column = super().get_user_input(super().get_data())
        if super().checkPosition(row, column):
            return row, column
        print("Position Occupied!")
        self.get_player_input()

    def get_computer_input(self):
        row, column = super().calculate_next_move(
            self.get_available_moves(), super().get_data()
        )
        print(f"Computer played: {row+1}, {column+1}")
        return row, column


if __name__ == "__main__":
    # game = Game()
    # game.display()
    # game.get_user_input()
    # game.get_user_input()
    # game.get_user_input()
    # game.get_user_input()
    # print("Game Over")
    # game.reset()
    # game.display()

    game = Game()
    game.display()
    GameOver = False
    while not GameOver:
        game.reset()
        game.set_empty()
        while True:
            print("Players Turn")
            row, column = game.get_player_input()
            game.update(row-1, column-1, player="X")
            if game.check_winner():
                break
            print("Computers' Turn")
            row, column = game.get_computer_input()
            game.update(row, column, "O")
            if game.check_winner():
                break

        if input("Play Again?: ").upper() == "N":
            GameOver = True
