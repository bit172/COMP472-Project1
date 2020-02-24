import numpy as np

from heuristics import h, h2
from node import Node

from queue import PriorityQueue
from pqItem import PQItem

from strategy import Strategy
from typing import List, IO


class BFS(Strategy):
    def find_solution(self, params: List, search_file: IO) -> Node:
        initial_board = Node(params[0], params[3])
        goal = np.zeros((params[0], params[0]), dtype=np.uint8)

        open_q = PriorityQueue()
        open_q.put(PQItem(h2(initial_board.v, params[0]), initial_board))

        closed = set()

        length = 0
        max_l = params[2]

        while length <= max_l:
            current = open_q.get()

            if current.node.string_v not in closed:
                closed.add(current.node.string_v)
                search_file.write(f"{current.node.h} {current.node.h} 0 " + current.node.string_v + "\n")
                length += 1
            else:
                continue

            if np.array_equal(current.node.v, goal):
                return current.node

            children = current.node.find_children(False)

            for child in children:
                child.p = current.node
                new_child = PQItem(child.h, child)
                open_q.put(new_child)
