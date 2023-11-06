import time

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the chessboard (n): "))
        if n <= 0:
            raise ValueError("Please enter a positive integer.")
        
        board = [[0] * n for _ in range(n)]

        # Place the first queen in the first row
        board[0][0] = 1

        print("\nBoard after placing the first queen :-")
        print_board(board)

        start_time = time.time()

        # Solve the n-queens problem
        if solve_n_queens(board, 1, n):
            print("\nFinal Solution :-")
            print_board(board)
        else:
            print("\nNo solution exists.")

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nTime taken by code to execute :- {execution_time:.6f} seconds")

    except ValueError as e:
        print(f"Error:- {e}")

