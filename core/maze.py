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

    def __ids_visited_len(self, visited):
        """Return length of visited blocks in ids"""

        arr = []
        for item in visited.values():
            arr.extend(item)
        return len(list(set(arr)))

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

    def ids_search(self):
        """IDS base on graph-search"""

        # Store visited nodes for each iteration
        visited = dict()
        # Do dls till end's depth reached
        depth = 0
        while True:
            path, visited[depth] = self.dls_search(
                self.start_block, self.end_block, depth, [])
            if path:
                return path, self.__ids_visited_len(visited)
            # If depth reaches 100 then return
            # To prevent infinite loop for unreachable end block unnecessary
            if depth == 100:
                return [], self.__ids_visited_len(visited)
            depth += 1

    def a_star_search(self):
        """A* search base on graph search"""

        # Create lists for open nodes and closed nodes
        open = []
        visited = []

        open.append(self.start_block)

        # Loop until the open list is empty
        while open:
            # Get the node with the lowest cost
            current_block = open[0]
            open.remove(current_block)
            visited.append(current_block.position)

            # Check if we have reached the goal, return the path
            if current_block.position == self.end_block.position:
                return self.init_path(current_block), len(visited)

            child = self.init_child(current_block)
            # Loop child
            for block in child:
                # Generate blocks in child heuristics
                block.g = current_block.g + 1
                # h = (delta(x) ^ 2) + (delta(y) ^ 2)
                block.h = pow(block.position[0] - self.end_block.position[0], 2) + pow(
                    block.position[1] - self.end_block.position[1], 2)
                # f = g + h
                block.f = block.g + block.h
                # Check if child is in open list and if it has a lower f value
                if self.add_to_open(open, block):
                    # check if current block (child) not in visited
                    if not visited.__contains__(block.position):
                        open.append(block)
                        # Sort blocks base on value of their f
                        sorted(open, key=lambda node_ob: node_ob.f)
        # Return None, no path is found
        return [], len(visited)

    def add_to_open(self, open, block):
        """Check if a child should be added to open list"""

        for node in open:
            if block.position == node.position and block.f >= node.f:
                return False
        return True
