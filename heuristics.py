def h(x):
    black = 0
    for i in range(len(x)):
        if x[i] == "1":
            black += 1
    return black


def h2(board, n):
    numPattern = 0
    totalBlack = 0

    for i in range(n):
        for j in range(n):
            if board[i, j]:
                totalBlack += 1
            if is_pattern(board, n, i, j):
                numPattern += 1
    return totalBlack - numPattern


def is_pattern(board, n, i, j):
    if (i + 1 >= n or board[i + 1, j]) \
            and (i - 1 < 0 or board[i - 1, j]) \
            and (j+1 >= n or board[i, j + 1]) \
            and (j-1 < 0 or board[i, j - 1]):
        return True
    return False
