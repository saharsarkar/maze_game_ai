class Node:
    def __init__(self, parent, position) -> None:
        self.parent = parent
        self.position = position

        self.h = 0
        self.g = 0
        self.f = 0


class Maze:

    def __init__(self, start, end, walls):

        self.FIRST_BLOCK = (0, 0)
        self.LAST_BLOCK = (19, 19)
        # start block with None parent
        self.start_block = Node(Node(None, None), start)
        self.end_block = Node(None, end)
        self.walls = walls

    def __grater_than_equal(self, tuple1, tuple2):
        return all(x >= y for x, y in zip(tuple1, tuple2))

    def __less_than_equal(self, tuple1, tuple2):
        return all(x <= y for x, y in zip(tuple1, tuple2))

    def init_path(self, current_block):
        """Path from root to goal"""

        path = []
        while current_block is not self.start_block:
            path.append(current_block.position)
            current_block = current_block.parent
        path.reverse()  # reversed path
        return path[:-1]  # return path without start and end block

    def init_child(self, block):

        # list for store children of the given block
        child = []
        # initial children position
        bottom_block = (block.position[0] - 1, block.position[1])
        left_block = (block.position[0], block.position[1] - 1)
        above_block = (block.position[0] + 1, block.position[1])
        right_block = (block.position[0], block.position[1] + 1)

        # add children in clockwise order (bottom, left, up, right)
        if self.__grater_than_equal(bottom_block, self.FIRST_BLOCK) and bottom_block != block.parent.position:
            child.append(Node(block, bottom_block))
        if self.__grater_than_equal(left_block, self.FIRST_BLOCK) and left_block != block.parent.position:
            child.append(Node(block, left_block))
        if self.__less_than_equal(above_block, self.LAST_BLOCK) and above_block != block.parent.position:
            child.append(Node(block, above_block))
        if self.__less_than_equal(right_block, self.LAST_BLOCK) and right_block != block.parent.position:
            child.append(Node(block, right_block))

        # remove children which are in walls
        child = [
            block for block in child if not self.walls.__contains__(block.position)]
        return child

    def bfs_search(self):
        """BFS base on graph search"""

        queue = []
        visited = []

        queue.append(self.start_block)
        visited.append(self.start_block.position)

        while queue:
            # give the first element of queue
            cur_block = queue[0]
            # remove the cur_block from queue
            queue.remove(cur_block)

            if cur_block.position == self.end_block.position:
                # return path and length of expanded blocks
                return self.init_path(cur_block), len(visited)
            child = self.init_child(cur_block)
            for block in child:
                if not visited.__contains__(block.position):
                    visited.append(block.position)
                    queue.append(block)
        return [], len(visited)

    def dls_search(self, src, end, depth, visited):
        """DSL base on graph search"""

        visited.append(src.position)

        if src.position == end.position:
            return self.init_path(src), visited
        # If reached the maximum depth, stop recursing.
        if depth <= 0:
            return [], visited
        child = self.init_child(src)
        # Recur for all the vertices adjacent to this vertex
        for block in child:
            # check the child wasn't visit yet
            if not visited.__contains__(block.position):
                path, visited = self.dls_search(
                    block, end, depth-1, visited)
                if path:
                    return path, visited
        return [], visited

    #TODO: a_star_search
