import numpy as np


class Node:
    def __init__(self, n, initial):
        board = np.zeros((n, n), dtype=np.int32)
        index = 0
        for i in range(n):
            for j in range(n):
                board[i, j] = initial[index]
                index += 1
        self.v = board

    def find_children(self):
        n = len(self.v[0])
        for i in range(n):
            for j in range(n):
                child = np.array(self.v)
                # change the touched token
                if child[i,j]:
                    child[i,j] = 0
                else:
                    child[i,j] = 1
                # left
                if j-1 > 0:
                    pass
                # right

                # top

                # bottom






