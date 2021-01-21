class Node:
    def __init__(self, parent, position) -> None:
        self.parent = parent
        self.position = position

        self.h = 0
        self.g = 0
        self.f = 0
