import sys

import numpy

checked = 2


def h(x):
    black = 0
    for i in range(len(x)):
        if x[i] == "1":
            black += 1
    return black


def h2(board, n):
    dup_board = numpy.empty_like(board)
    dup_board[:] = board
    numPattern = 0
    totalBlack = 0
    overlap = 0

    for i in range(n - 1):
        for j in range(n - 1):
            if board[i, j] == 1:
                totalBlack += 1
            if check_pattern(board, i, j):
                numPattern += 1
                overlap += mark_pattern(dup_board, i, j)
    return (totalBlack + overlap) / float(numPattern + 1)


def check_pattern(ini_board, i, j):
    if (ini_board[i + 1, j] is None or ini_board[i + 1, j]) \
            and (ini_board[i - 1, j] is None or ini_board[i - 1, j]) \
            and (ini_board[i, j + 1] is None or ini_board[i, j + 1]) \
            and (ini_board[i, j - 1] or ini_board[i, j - 1]):
        return True
    return False


def mark_pattern(dup_board, i, j):
    dup_board[i, j] = checked
    return mark(dup_board[i + 1, j]) + mark(dup_board[i - 1, j]) + mark(dup_board[i, j + 1]) + mark(dup_board[i, j - 1])


def mark(x):
    if x == 1:
        x = checked
    elif x == checked:
        return 1
    return 0
