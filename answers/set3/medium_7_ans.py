def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the given player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(" " not in row for row in board)

def get_player_input(player):
    """Gets valid player input for row and column."""
    while True:
        try:
            row = int(input(f"Player {player}, choose row (1-3): ")) - 1
            col = int(input(f"Player {player}, choose column (1-3): ")) - 1
            if not (0 <= row <= 2 and 0 <= col <= 2):
                raise ValueError
            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")

def tic_tac_toe():
    """Runs the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row, col = get_player_input(current_player)
        
        if board[row][col] != " ":
            print("This cell is already taken. Try again.")
            continue
        
        board[row][col] = current_player
               
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()