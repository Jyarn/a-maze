import time


class Node:
    """
    Represents a block; Start, Empty, Wall, or End
    """

    def __init__(self, type, id):
        """Creates instance of node/block/spot on the maze

        Parameters
        ----------
        type : string
            Placeholder for the item in the maze
        id : int
            Unique ID to identify the node
        """
        self.type = type
        self.id = id
        self.visited = False
        self.connection = 0


class SolveBFS:
    def __init__(self, maze, start, end, open, wall):
        """Creates an instance of a maze.

        Parameters
        ----------
        maze : 2d list
            A 2d list of the maze.
        start : string
            Start node on the maze.
        end : string
            Exit node on the maze.
        open : string
            Open path on the maze.
        wall : string
            Obstacle on the maze.
        """
        self.maze = maze
        self.start = start
        self.end = end
        self.open = open
        self.wall = wall

        self.last = 0
        self.time = 0  # time to solve maze
        self.searched = 0

        self.add_outline()
        self.create_id_nodes()
        self.solve()

    def add_outline(self):
        """Adds an outline at the start and end of maze to avoid KeyError issues"""

        # add left and right walls in each row
        maze_rows = len(self.maze)
        for row in range(maze_rows):
            self.maze[row].insert(0, ".")
            self.maze[row].append(".")

        # add top and bottom rows
        border = ["."] * len(self.maze[0])
        self.maze.insert(0, border)
        self.maze.append(border)

        # print()
        # [print(i) for i in self.maze]
        # print()

    def remove_outline(self):
        """Removes outline from maze for displaying to user"""

        # remove left and right walls in each row
        maze_rows = len(self.maze)
        for row in range(maze_rows):
            self.maze[row].pop(0)
            self.maze[row].pop()

        # remove top and bottom rows
        self.maze.pop(0)
        self.maze.pop()

        # print()
        # [print(i) for i in self.maze]
        # print()

    def create_id_nodes(self):
        """Converts the 2d list into a dictionary containing IDs for locations"""

        # dictionary of ids presenting node objects
        self.nodes = {}
        # unique node ids
        set_id = 0

        maze_rows = len(self.maze)
        maze_cols = len(self.maze[0])

        # loop through each node and record its object id
        for row in range(maze_rows):
            for col in range(maze_cols):
                set_id += 1
                node_type = self.maze[row][col]

                if node_type == self.start:
                    self.start_id = set_id
                elif node_type == self.end:
                    self.end_id = set_id

                node = Node(node_type, set_id)
                self.nodes[set_id] = node

    def solve(self):
        """Finds the path from start to finish using the Breadth-first search Algo"""

        queue = []
        maze_cols = len(self.maze[0])

        curr_node = self.nodes[self.start_id]
        curr_node.visited = True
        queue.append(curr_node)

        self.time = time.time()
        found = False
        while not found:
            self.searched += 1

            # get first node
            try:
                curr_node = queue[0]
            # if exit node not within path then queue is empty since all open nodes were visited
            except IndexError as e:
                print("solve queue", e)
                break

            # get id of left, right, up, and down nodes
            adj_nodes = [
                curr_node.id - 1,
                curr_node.id + 1,
                curr_node.id - maze_cols,
                curr_node.id + maze_cols,
            ]

            # loop through neighbors and add to queue
            for adj_node in adj_nodes:
                try:
                    if not self.nodes[adj_node].visited:
                        # 0 is default, ie only store first open node visited
                        if self.nodes[adj_node].connection == 0:
                            self.nodes[adj_node].connection = curr_node
                        # if node is open
                        if self.nodes[adj_node].type == self.open:
                            queue.append(self.nodes[adj_node])
                        # exit node reached
                        elif self.nodes[adj_node].type == self.end:
                            found = True
                            self.last = self.nodes[adj_node]

                        self.nodes[adj_node].visited = True
                except Exception as e:
                    print("solve loop", e)
                    pass
            queue.pop(0)

        # Done solving
        self.time = time.time() - self.time
        print(">Solve stats")
        print("Searched through", self.searched, "open nodes")
        print("Time taken:", self.time)

    def show(self):
        """Prints the maze and its solution to the console"""
        connected = False
        last = self.last
        while not connected:
            try:
                last = last.connection
                if last.type != self.start:
                    last.type = "+"
            # when no exit node is found or last item reached
            except AttributeError:
                break

        print("Solution:")
        maze_rows = len(self.maze)
        maze_cols = len(self.maze[0])
        id = 0
        for _ in range(1, maze_rows):
            for _ in range(maze_cols):
                id += 1
                print(self.nodes[id].type.center(2), end="")
            print()
