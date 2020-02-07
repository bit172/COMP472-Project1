import numpy as np
from node import Node

f = open('input.txt', "r")
# Converts all inputs into ints except the last one
params = [int(val) if idx < 2 else val for idx, val in enumerate(f.read().split(" "))]

initial_board = Node(params[0], params[2])
goal = np.zeros((params[0], params[0]), dtype=np.uint8)
max_d = params[1]


def exists_in_closed(closed_list, current):
    """
    Checks if a board state exists in the closed_list

    :param closed_list: closed list
    :param current: board to test
    :return: if the board is in the closed list
    """

    exists = False
    for b in closed_list:
        if np.array_equal(b, current):
            exists = True
            break
    return exists


def dfs():
    # Open Stack with elements like (current board value, parent, depth)
    open_stack = [(initial_board, 1)]
    closed_list = []

    while open_stack:
        current = open_stack.pop()
        if not exists_in_closed(closed_list, current[0].v):
            closed_list.append(current[0].v)
        else:
            continue
        depth = current[1] + 1

        if np.array_equal(current[0].v, goal):
            return current[0]

        if depth <= max_d:
            children = current[0].find_children()
            for child in children:
                if not exists_in_closed(closed_list, child):
                    child.p = current[0]
                    open_stack.append((child, depth))


if __name__ == '__main__':
    sol_node = dfs()
    parent = sol_node
    while parent:
        print(parent.v)
        print(parent.touched)
        parent = parent.p
