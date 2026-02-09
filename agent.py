import copy








class Agent:


    def __init__(self, agent, player):
        self.ai = agent
        self.human = player

    def check_winning_move(board):
        global ai
        ROW_COUNT = len(board)
        COLUMN_COUNT = len(board[0])
        # Check horizontal locations
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if (board[r][c] == ai and board[r][c + 1] == ai and
                        board[r][c + 2] == ai and board[r][c + 3] == ai):
                    return True
        # Check vertical locations
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT):
                if (board[r][c] == ai and board[r + 1][c] == ai and
                        board[r + 2][c] == ai and board[r + 3][c] == ai):
                    return True
        # Check positively sloped diagonals
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                if (board[r][c] == ai and board[r + 1][c + 1] == ai and
                        board[r + 2][c + 2] == ai and board[r + 3][c + 3] == ai):
                    return True
        # Check negatively sloped diagonals
        for r in range(3, ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if (board[r][c] == ai and board[r - 1][c + 1] == ai and
                        board[r - 2][c + 2] == ai and board[r - 3][c + 3] == ai):
                    return True
        return False

    def can_play_column(self, state, col):
        for i in range(6):
            if state[i][col] == ' ':
                return True
        return False

    def move_score(self, state, col, move_count):
        if move_count >= 42:
            return 0
        for i in range(7):
            if self.can_play_column(state, i):
                for j in range(5,-1,-1):
                    if state[j][i] == ' ':
                        state[j][i] = self.ai
                        break
                if self.check_winning_move(state):
                    return (43 - move_count)/2

        best_score = -42


        return None


    def play(self, state, move_count):
        board_copy = copy.deepcopy(state)
        if move_count >= 42:
            return 0
        best_score = 0
        index = -1
        for i in range(7):
            if self.can_play_column(state, i):
                for j in range(5,-1,-1):
                    if board_copy[j][i] == ' ':
                        board_copy[j][i] = self.ai
                        break
                new_score = self.move_score(board_copy, i, move_count + 1)
                if new_score > best_score:
                    best_score = new_score
                    index = i

        return index
