def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, N):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, N):
                return True
            board[row][col] = 0  # Backtrack if the placement doesn't lead to a solution

    return False

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[0][0] = 1  # Placing the first queen in the top-left corner

    if not solve_nqueens(board, 1, N):
        print("No solution exists")
        return

    print("Solution:")
    print_solution(board, N)

if __name__ == "__main__":
    N = int(input("enter number of queens"))  # Change N to the desired board size
    nqueens(N)
