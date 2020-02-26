import numpy as np

from heuristics import h2
from node import Node

from queue import PriorityQueue
from pqAStarItem import PQAStarItem
from strategy import Strategy
from typing import List, IO


class A_star(Strategy):
    def find_solution(self, params: List, search_file: IO) -> Node:
        initial_board = Node(params[0], params[3])
        goal = np.zeros((params[0], params[0]), dtype=np.uint8)

        depth = 1
        open_q = PriorityQueue()
        open_q.put(PQAStarItem(depth, h2(initial_board.v, params[0]), initial_board))
        # open_q.put(PQItem(h(initial_board.string_v), initial_board))

        closed = set()

        length = 0
        max_l = params[2]

        while length <= max_l:
            current = open_q.get()
            depth = current.g + 1
            if current.node.string_v not in closed:
                closed.add(current.node.string_v)
                search_file.write(f"{current.f} {current.g} {current.h} " + current.node.string_v + "\n")
                length += 1
            else:
                continue

            if np.array_equal(current.node.v, goal):
                return current.node

            children = current.node.find_children(False)

            for child in children:
                h = h2(child.v, params[0])
                child.p = current.node
                new_child = PQAStarItem(depth, h, child)
                open_q.put(new_child)
