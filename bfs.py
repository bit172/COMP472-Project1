import numpy as np

from heuristics import h, h1
from node import Node

from queue import PriorityQueue
from pq_bfs_item import PQBFSItem

from strategy import Strategy
from typing import List, IO


class BFS(Strategy):
    def find_solution(self, params: List, search_file: IO) -> Node:
        initial_board = Node(params[0], params[3])
        goal = np.zeros((params[0], params[0]), dtype=np.uint8)
        open_q = PriorityQueue()
        open_q.put(PQBFSItem(h(initial_board.v, params[0]), initial_board))
        # open_q.put(PQBFSItem(h1(initial_board.string_v), initial_board))

        closed = set()
        length = 0
        max_l = params[2]

        while length <= max_l:
            current = open_q.get()
            if current.node.string_v not in closed:
                closed.add(current.node.string_v)
                search_file.write(f"{current.h} {current.h} 0 " + current.node.string_v + "\n")
                length += 1
            else:
                continue

            if np.array_equal(current.node.v, goal):
                return current.node

            children = current.node.find_children(False)
            for child in children:
                child.p = current.node
                new_child = PQBFSItem(h(child.v, params[0]), child)
                # new_child = PQBFSItem(h1(child.string_v), child)
                open_q.put(new_child)
