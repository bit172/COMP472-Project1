import numpy as np
from node import Node

f = open('input.txt', "r")
# Converts all inputs into ints except the last one
params = [int(val) if idx < 2 else val for idx, val in enumerate(f.read().split(" "))]

initial_board = Node(params[0], params[2])
goal = np.zeros((params[0], params[0]), dtype=np.uint8)
max_d = params[1]


def exists_in_closed(closed_list, current):
    exists = False
    for b in closed_list:
        if np.array_equal(b, current):
            exists = True
            break
    return exists


def dfs():
    # Open Stack with elements like (current board value, parent, depth)
    open_stack = [(initial_board, 1)]
    closed_list = set()

    while open_stack:
        current = open_stack.pop()
        closed_list.add(current[0].string_v)
        depth = current[1] + 1

        if np.array_equal(current[0].v, goal):
            return current[0]

        if depth <= max_d:
            children = current[0].find_children()
            for child in children:
                if child.string_v not in closed_list:
                    child.p = current[0]
                    open_stack.append((child, depth))


if __name__ == '__main__':
    sol_node = dfs()
    parent = sol_node
    if not parent:
        print("no solution")
    while parent:
        print(parent.v)
        print(parent.touched)
        parent = parent.p
