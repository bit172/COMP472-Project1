import numpy as np


def stringify(board):
    s = ""
    for i in range(Node.n):
        for j in range(Node.n):
            s += str(board[i, j])
    return s


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
        # State of board
        self.v = board
        # String value of board
        self.string_v = stringify(board)
        # Parent of board
        self.p = None
        # Position of touched token to get to current board
        self.touched = None

    def find_children(self):
        # Data type of the string_child array which consists of
        # a string representation of the state of the child board and
        # a string for the position of the token touched to reach it
        dt = np.dtype([('child', np.unicode_, Node.n ** 2), ('touched', np.unicode_, 2)])
        string_children = np.empty([Node.n ** 2], dtype=dt)
        children = np.empty([Node.n ** 2], dtype=object)
        index = 0
        for i in range(Node.n):
            for j in range(Node.n):
                # copy the current state of the board
                child = np.array(self.v)
                # change the touched token
                touched = str(i) + str(j)
                if child[i, j]:
                    child[i, j] = 0
                else:
                    child[i, j] = 1
                # left
                if j - 1 >= 0:
                    if child[i, j - 1]:
                        child[i, j - 1] = 0
                    else:
                        child[i, j - 1] = 1
                # right
                if j + 1 <= Node.n - 1:
                    if child[i, j + 1]:
                        child[i, j + 1] = 0
                    else:
                        child[i, j + 1] = 1
                # top
                if i - 1 >= 0:
                    if child[i - 1, j]:
                        child[i - 1, j] = 0
                    else:
                        child[i - 1, j] = 1
                # bottom
                if i + 1 <= Node.n - 1:
                    if child[i + 1, j]:
                        child[i + 1, j] = 0
                    else:
                        child[i + 1, j] = 1
                # insert the child and the position
                string_children[index]["child"] = stringify(child)
                string_children[index]["touched"] = touched
                index += 1
        # sort the children (in reverse order for adding to stack)
        string_children[::-1].sort()
        # create the nodes using the string version of the board
        for idx, string_child in enumerate(string_children):
            children[idx] = Node(Node.n, string_child["child"])
            children[idx].touched = string_child["touched"]
        return children
