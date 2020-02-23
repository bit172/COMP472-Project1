class PQItem:
    def __init__(self, h, node):
        self.h = h
        self.node = node

    def __lt__(self, other):
        return self.h < other.h
