class PQAStarItem:
    def __init__(self,  g, h, node):
        self.g = g
        self.h = h
        self.f = g + h
        self.node = node

    def __lt__(self, other):
        if self.h == other.h:
            return self.node.string_v < other.node.string_v
        return self.f < other.f
