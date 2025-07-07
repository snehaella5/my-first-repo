# Simple text-based Tic Tac Toe for 2 players

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in zip(*board):
        if all([cell == player for cell in col]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        try:
            row = int(input(f"{current_player}, enter row (0-2): "))
            col = int(input(f"{current_player}, enter column (0-2): "))
        except ValueError:
            print(" Invalid input! Use numbers 0-2.")
            continue

        if board[row][col] != " ":
            print(" That spot is taken! Try again.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw! 🤝")

if __name__ == "__main__":
    play_game()
1