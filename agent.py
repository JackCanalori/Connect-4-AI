import copy


class Agent:
    def __init__(self, agent_piece, player_piece):
        self.ai = agent_piece
        self.human = player_piece

    def is_winner(self, board, piece):
        # Check horizontal, vertical, and diagonals for a specific piece
        rows, cols = 6, 7
        for r in range(rows):
            for c in range(cols - 3):
                if all(board[r][c+i] == piece for i in range(4)): return True
        for r in range(rows - 3):
            for c in range(cols):
                if all(board[r+i][c] == piece for i in range(4)): return True
        for r in range(rows - 3):
            for c in range(cols - 3):
                if all(board[r+i][c+i] == piece for i in range(4)): return True
        for r in range(3, rows):
            for c in range(cols - 3):
                if all(board[r-i][c+i] == piece for i in range(4)): return True
        return False

    def get_valid_locations(self, board):
        return [c for c in range(7) if board[0][c] == ' ']

    def get_next_open_row(self, board, col):
        for r in range(5, -1, -1):
            if board[r][col] == ' ':
                return r

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.is_winner(board, self.ai) or self.is_winner(board, self.human) or len(valid_locations) == 0

        if depth == 0 or is_terminal:
            if is_terminal:
                if self.is_winner(board, self.ai): return (None, 10000000)
                elif self.is_winner(board, self.human): return (None, -10000000)
                else: return (None, 0) # Draw
            else: return (None, 0)

        if maximizingPlayer:
            value = -float('inf')
            column = valid_locations[0]
            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                temp_board = copy.deepcopy(board)
                temp_board[row][col] = self.ai
                new_score = self.minimax(temp_board, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta: break
            return column, value

        else: # Minimizing player
            value = float('inf')
            column = valid_locations[0]
            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                temp_board = copy.deepcopy(board)
                temp_board[row][col] = self.human
                new_score = self.minimax(temp_board, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta: break
            return column, value

    def play(self, state, move_count):
        col, score = self.minimax(state, 10, -float('inf'), float('inf'), True)
        return col