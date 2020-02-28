class PQBFSItem:
    def __init__(self, h, node):
        self.h = h
        self.node = node

    def __lt__(self, other):
        if self.h == other.h:
            return self.node.string_v < other.node.string_v
        return self.h < other.h
