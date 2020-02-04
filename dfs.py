import numpy as np
from node import Node

f = open('input.txt', "r")
# Converts all inputs into ints except the last one
params = [int(val) if idx < 2 else val for idx, val in enumerate(f.read().split(" "))]

initial_board = Node(params[0], params[2])
goal = np.zeros((params[0], params[0]), dtype=int)
max_d = params[1]


def dfs():
    # Open Stack with elements like (current board value, parent, depth)
    open_stack = [(initial_board, None, 1)]
    closed_list = []

    while open_stack:
        current = open_stack.pop()
        closed_list.append(current)
        depth = current[2] + 1

        if np.array_equal(current, goal):
            return closed_list

        if depth <= max_d:
            pass


if __name__ == '__main__':
    dfs()
