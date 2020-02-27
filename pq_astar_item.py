class PQAStarItem:
    def __init__(self,  g, h, node):
        self.g = g
        self.h = h
        self.f = g + h
        self.node = node

    def __lt__(self, other):
        return self.f < other.f
