import sys
import time
import queue
import copy
from termcolor import colored
import colorama

colorama.init()


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
        id : tuple
            Unique ID to identify the node
        """
        self.type = type
        self.id = id
        self.visited = False
        self.connection = 0


class MazeSolver:
    def __init__(self, maze, start, end, open, wall, path="+", verbose=False):
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
            Open node on the maze.
        wall : string
            Obstacle on the maze.
        path : string
            To draw the path from start to end.
        verbose : string
            Display the number of searches and time.
        """
        self.maze = copy.deepcopy(maze)
        self.start = start
        self.end = end
        self.open = open
        self.wall = wall
        self.path = path
        self.verbose = verbose

        self.last = 0
        self.time = 0  # time to solve maze
        self.searched = 0

        self.create_nodes()

    def create_nodes(self):
        self.nodes = {}

        maze_rows = len(self.maze)
        maze_cols = len(self.maze[0])

        # loop through each node and record its object id
        for row in range(maze_rows):
            for col in range(maze_cols):
                node_type = self.maze[row][col]

                if node_type == self.start:
                    self.start_node = (col, row)
                elif node_type == self.end:
                    self.end_node = (col, row)

                node = Node(node_type, (col, row))
                self.nodes[(col, row)] = node

        # check if start/end points don't exist or couldn't be identified
        if not hasattr(self, "start_node"):
            print("No start point found")
            sys.exit(1)
        elif not hasattr(self, "end_node"):
            print("No exit point found")
            sys.exit(1)

    def show(self):
        """Prints the maze and its solution to the console"""
        connected = False
        last = self.last
        # check if a solution was found
        if last == 0:
            print("No solution found")
        else:
            print("Solution:")

        while not connected:
            try:
                last = last.connection
                if last.type != self.start:
                    last.type = self.path
            # when no exit node is found or last item reached
            except AttributeError:
                break

        maze_rows = len(self.maze)
        maze_cols = len(self.maze[0])
        for row in range(maze_rows):
            for col in range(maze_cols):
                node_type = self.nodes[(col, row)].type
                if node_type == self.path:
                    print(colored(node_type, "green").center(2), end="")
                elif node_type == self.start or node_type == self.end:
                    print(colored(node_type, "white").center(2), end="")
                else:
                    print(colored(node_type, "cyan").center(2), end="")
            print()
        print()


class SolveBfsDfs(MazeSolver):
    """Finds a path from start to end using two very similar algorithrms:
    Breadth-first search and Depth-first search.

    Parameters
    ----------
    MazeSolver : class
        Creates class for the given maze
    """

    def __init__(self, maze, start, end, open, wall, path="+", verbose=False):
        MazeSolver.__init__(self, maze, start, end, open, wall, path, verbose)

    def solve(self, queue, algo):
        """Finds the path from start to finish and records the connections between the nodes.

        Parameters
        ----------
        queue : queue.Queue()/queue.LifoQueue()
            Handles FIFO or LIFO, quicker than appending/popping from list
        algo : string
            Name of algorithm for printing the stats
        """
        self.queue = queue
        curr_node = self.nodes[self.start_node]
        curr_node.visited = True
        self.queue.put(curr_node)

        self.time = time.time()
        found = False
        while not found:
            self.searched += 1

            # get runner up node
            if not self.queue.empty():
                curr_node = self.queue.get()
            else:
                break

            # get id of left, right, up, and down nodes
            # (x, y)
            adj_nodes = [
                (curr_node.id[0] - 1, curr_node.id[1]),
                (curr_node.id[0] + 1, curr_node.id[1]),
                (curr_node.id[0], curr_node.id[1] - 1),
                (curr_node.id[0], curr_node.id[1] + 1),
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
                            self.queue.put(self.nodes[adj_node])
                        # exit node reached
                        elif self.nodes[adj_node].type == self.end:
                            found = True
                            self.last = self.nodes[adj_node]

                        self.nodes[adj_node].visited = True
                # outside boundary
                except KeyError:
                    pass

        # Done solving
        self.time = time.time() - self.time
        if self.verbose:
            print(f">{algo} Solve Stats")
            print("Searched through", self.searched, "open nodes")
            print("Time taken:", self.time)


class SolveBfs(SolveBfsDfs):
    def __init__(self, maze, start, end, open, wall, path="+", verbose=False):
        """Finds path from start to end of maze using the Breadth-first search via FIFO Queues"""
        SolveBfsDfs.__init__(self, maze, start, end, open, wall, path, verbose)
        self.solve(queue.Queue(), "BFS")


class SolveDfs(SolveBfsDfs):
    def __init__(self, maze, start, end, open, wall, path="+", verbose=False):
        """Finds path from start to end of maze using the Depth-first search via LIFO Queues"""
        SolveBfsDfs.__init__(self, maze, start, end, open, wall, path, verbose)
        self.solve(queue.LifoQueue(), "DFS")
