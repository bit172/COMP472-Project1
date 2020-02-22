import numpy as np

from heuristics import h
from node import Node
from queue import PriorityQueue

from strategy import Strategy
from typing import List, IO


class BFS(Strategy):
    def find_solution(self, params: List, search_file: IO) -> Node:
        open_q = PriorityQueue()
        closed = set()
        current = open_q.get()
        length = 0
        max_l = params[2]
        goal = np.zeros((params[0], params[0]), dtype=np.uint8)

        while length <= max_l:
            if current not in closed:
                closed.add(current)
                length += 1
            else:
                continue

            if np.array_equal(current[1].v, goal):
                return current

            for child in current.find_children():
                new_child = (h(child), child)
                open_q.put(new_child)
