import numpy as np
from node import Node

from typing import List, IO
from strategy import Strategy


class DFS(Strategy):
    def find_solution(self, params: List, search_file: IO) -> Node:
        initial_board = Node(params[0], params[3])
        goal = np.zeros((params[0], params[0]), dtype=np.uint8)
        max_d = params[1]
        # Open Stack with elements like (current board value, parent, depth)
        open_stack = [(initial_board, 1)]
        closed_set = set()

        while open_stack:
            current = open_stack.pop()
            # adding depth to closed_set
            # closed_set.add((current[0].string_v, current[1]))

            # adding the board only
            closed_set.add(current[0].string_v)
            search_file.write("0 0 0 " + current[0].string_v + "\n")
            depth = current[1] + 1

            if np.array_equal(current[0].v, goal):
                return current[0]

            if depth <= max_d:
                children = current[0].find_children()
                for child in children:
                    # checking for the board only
                    if child.string_v not in closed_set:
                        # checking for the board and depth
                        # if (child.string_v, depth) not in closed_set:
                        child.p = current[0]
                        open_stack.append((child, depth))
