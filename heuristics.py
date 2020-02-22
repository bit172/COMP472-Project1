from node import Node


def h(self, x):
    black = 0
    for i in range(Node.n):
        for j in range(Node.n):
            if self[i, j] == 1:
                black += 1
    return black
