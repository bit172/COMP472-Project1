from node import Node


def h(x):
    black = 0
    for i in range(Node.n):
        for j in range(Node.n):
            if x[i, j] == 1:
                black += 1
    return black
