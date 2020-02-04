import numpy as np


class Node:
    n = 0

    def __init__(self, n, initial):
        Node.n = n
        board = np.zeros((n, n), dtype=np.uint8)
        index = 0
        for i in range(n):
            for j in range(n):
                board[i, j] = initial[index]
                index += 1
        self.v = board

    def find_children(self):
        children = np.empty([Node.n**2], dtype=object)

        for i in range(Node.n):
            for j in range(Node.n):
                # copy the current state of the board
                child = np.array(self.v)
                # change the touched token
                if child[i, j]:
                    child[i, j] = 0
                else:
                    child[i, j] = 1
                # left
                if j - 1 > 0:
                    pass
                # right

                # top

                # bottom
