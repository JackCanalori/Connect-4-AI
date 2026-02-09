import agent
ai_piece = 'O'
human_piece = 'X'
ai = agent.Agent(ai_piece, human_piece)
move_count = 0
board = [[' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ']]

def print_board():
    print("+---------------------------------+")
    for row in board:
        for col in row:
            print("|", col, "|", end='')
        print("\n+---------------------------------+")

def can_play_column(col):
    for i in range(6):
        if board[i][col] == ' ':
            return True
    return False

def play_column(col):
    global move_count
    for i in range(5, -1, -1):
        if board[i][col] == ' ':
            board[i][col] = human_piece
            move_count += 1
            return True
    return False

def ai_play(col):
    global move_count
    for i in range(5, -1, -1):
        if board[i][col] == ' ':
            board[i][col] = ai_piece
            move_count += 1
            return True
    return False

def check_win(piece):
   ROW_COUNT = len(board)
   COLUMN_COUNT = len(board[0])
   # Check horizontal locations
   for r in range(ROW_COUNT):
       for c in range(COLUMN_COUNT - 3):
           if (board[r][c] == piece and board[r][c + 1] == piece and
               board[r][c + 2] == piece and board[r][c + 3] == piece):
               return True
   # Check vertical locations
   for r in range(ROW_COUNT - 3):
       for c in range(COLUMN_COUNT):
           if (board[r][c] == piece and board[r + 1][c] == piece and
               board[r + 2][c] == piece and board[r + 3][c] == piece):
               return True
   # Check positively sloped diagonals
   for r in range(ROW_COUNT - 3):
       for c in range(COLUMN_COUNT - 3):
           if (board[r][c] == piece and board[r + 1][c + 1] == piece and
               board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece):
               return True
   # Check negatively sloped diagonals
   for r in range(3, ROW_COUNT):
       for c in range(COLUMN_COUNT - 3):
           if (board[r][c] == piece and board[r - 1][c + 1] == piece and
               board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece):
               return True
   return False

def main():
    while True:
        print("Player enter column number to put your piece:")
        print_board()
        col = int(input())
        while not can_play_column(col):
            print("Enter a valid column number:")
            print_board()
            col = int(input())
        play_column(col)
        ai_play(ai.play(board, move_count))

        if check_win(ai_piece):
            print("AI Wins")
            print_board()
            break
        if check_win(human_piece):
            print("Human Wins")
            print_board()
            break
        if (move_count == 42):
            print("Tie Game")
            print_board()
            break

main()



