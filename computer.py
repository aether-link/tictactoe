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
board1= [
    ["X", "O", "X"],
    [" ", "O", " "],
    ["O", "X", " "]
]

board2 = [
    ["X", "O", "X"],
    [" ", "O", " "],
    ["O", "X", "X"]
]

board3 = [
    ["X", "O", "X"],
    [" ", "O", " "],
    ["O", "X", "O"]
]

class Computer:
    defaultBoard = [[" " for _ in range(3)] for _ in range(3)]
    def __init__(self, computer="O",player="X"):
        self.computer=computer
        self.player=player
    
    def get_moves(self, board, symbol):
        moves = []
        for row in range(3):
            for column in range(3):
                if board[row][column] == symbol:
                    moves.append((row, column))
        return moves
    
    def get_available_moves(self,board):
       return self.get_moves(board, " ")
   
    def get_player_moves(self,board):
       return self.get_moves(board, self.player)

    def get_computer_moves(self,board):
       return self.get_moves(board, self.computer)
   
    def check_winner(self, board, symbol, winning_conditions=winning_conditions):
       for condition in winning_conditions:
           if all(board[row][column] == symbol for row, column in condition):
               return True
       return False
       
    def calculate_next_move(self, board):
        available_moves = self.get_available_moves(board)
        for move in available_moves:
            row, column = move
            board[row][column] = self.computer
            if self.check_winner(board, self.computer):
                return row, column
            board[row][column] = " "
        for move in available_moves:
            row, column = move
            board[row][column] = self.player
            if self.check_winner(board, self.player):
                return row, column
            board[row][column] = " "
        return available_moves[0]
    

if __name__ == "__main__":
    computer = Computer()
    print(computer.calculate_next_move(board1))
    print(computer.calculate_next_move(board2))
    print(computer.calculate_next_move(board3))