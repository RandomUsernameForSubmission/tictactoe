class GameState:
    def __init__(self, player_pawn, board_size: int = 3):
        self.player_pawn = player_pawn
        self.computer_pawn = 'O' if self.player_pawn == 'X' else 'X'
        self.board_size = min(board_size, 10)
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def move(self, pawn, x, y):
        if self.board[y][x] != '':
            return False
        self.board[y][x] = pawn
        return True

    def get_empty_cells(self):
        return [(x, y) for y in range(self.board_size) for x in range(self.board_size)
                if self.board[y][x] == '']

    def is_draw(self):
        return all(cell != '' for row in self.board for cell in row)

    def check_win(self, pawn):
        for row in self.board:
            if all(cell == pawn for cell in row):
                return True
        for col in range(self.board_size):
            if all(self.board[row][col] == pawn for row in range(self.board_size)):
                return True
        if all(self.board[i][i] == pawn for i in range(self.board_size)):
            return True
        if all(self.board[i][self.board_size - 1 - i] == pawn for i in range(self.board_size)):
            return True
        return False
    
    def reset_state(self, new_player_pawn):
        self.player_pawn = new_player_pawn
        self.computer_pawn = 'O' if self.player_pawn == 'X' else 'X'
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
