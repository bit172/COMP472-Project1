import numpy as np
from node import Node

f = open('input.txt', "r")
# Converts all inputs into ints except the last one
params = [int(val) if idx < 2 else val for idx, val in enumerate(f.read().split(" "))]

initial_board = Node(params[0], params[2])
goal = np.zeros((params[0], params[0]), dtype=np.uint8)
max_d = params[1]


def dfs():
    # Open Stack with elements like (current board value, parent, depth)
    open_stack = [(initial_board, None, 1)]
    closed_list = []

    while open_stack:
        current = open_stack.pop()
        closed_list.append(current)
        depth = current[2] + 1

        if np.array_equal(current[0].v, goal):
            return closed_list

        if depth <= max_d:
            children = current[0].find_children()
            for child in children:
                if child not in closed_list:
                    open_stack.append((child, current[0], depth))
        else:
            continue


if __name__ == '__main__':
    for x in dfs():
        print(x[0].v)

