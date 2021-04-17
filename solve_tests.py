import solve

maze1 = [
    [" ", "#", "S"],
    [" ", " ", "#"],
    [" ", " ", "#"],
    ["#", " ", " "],
    ["#", "E", "#"],
]

maze2 = [
    ["S", " ", "#"],
    [" ", " ", "#"],
    [" ", " ", " "],
    ["E", "#", "#"],
]

maze3 = [
    ["#", "#", "S", "#"],
    ["#", " ", " ", "#"],
    [" ", " ", "#", "#"],
    [" ", "#", " ", "#"],
    [" ", " ", "#", "#"],
    [" ", " ", "#", "#"],
    ["#", " ", " ", "#"],
    ["#", "#", "E", "#"],
]

maze4 = [
    ["#", "#", "#", "#", "#", "S", "#"],
    [" ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", "#", "#"],
    ["#", "#", "#", "E", "#", "#", "#"],
]

maze5 = [
    ["#", "#", "#", "S", "#", "#", "#"],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "#", "#", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "#", "#", "#", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "#", " ", "#", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    ["#", "#", "#", "E", "#", "#", "#"],
]

maze6 = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]

maze7 = [list(i) for i in maze6]

maze8 = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++ +++     ++          ++    +++++++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+      ++ +++++++ +++     ++          ++    +++++++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]

maze9 = [
    "S        E",
    "          ",
    "          ",
    "          ",
    "          ",
    "          ",
]

# Time tests between different maze sizes
def bfs_maze_sizes(n):
    p = []
    [p.append(0) for _ in range(8)]
    for _ in range(n):
        maze = solve.SolveBfs(maze1, "S", "E", " ", "#")
        p[0] += maze.searched / maze.time

        maze = solve.SolveBfs(maze2, "S", "E", " ", "#")
        p[1] += maze.searched / maze.time

        maze = solve.SolveBfs(maze3, "S", "E", " ", "#")
        p[2] += maze.searched / maze.time

        maze = solve.SolveBfs(maze4, "S", "E", " ", "#")
        p[3] += maze.searched / maze.time

        maze = solve.SolveBfs(maze5, "S", "E", " ", "#")
        p[4] += maze.searched / maze.time

        maze = solve.SolveBfs(maze6, "s", "e", " ", "+", ".")
        p[5] += maze.searched / maze.time

        maze = solve.SolveBfs(maze7, "s", "e", " ", "+", ".")
        p[6] += maze.searched / maze.time

        maze = solve.SolveBfs(maze8, "s", "e", " ", "+", ".")
        p[7] += maze.searched / maze.time

    if n != 0:
        [print(f"bfs maze {i+1}", p[i] / n, "nodes/s") for i in range(len(p))]
        print()


def dfs_maze_sizes(n):
    p = []
    [p.append(0) for _ in range(9)]
    for _ in range(n):
        maze = solve.SolveDfs(maze1, "S", "E", " ", "#")
        p[0] += maze.searched / maze.time

        maze = solve.SolveDfs(maze2, "S", "E", " ", "#")
        p[1] += maze.searched / maze.time

        maze = solve.SolveDfs(maze3, "S", "E", " ", "#")
        p[2] += maze.searched / maze.time

        maze = solve.SolveDfs(maze4, "S", "E", " ", "#")
        p[3] += maze.searched / maze.time

        maze = solve.SolveDfs(maze5, "S", "E", " ", "#")
        p[4] += maze.searched / maze.time

        maze = solve.SolveDfs(maze6, "s", "e", " ", "+", ".")
        p[5] += maze.searched / maze.time

        maze = solve.SolveDfs(maze7, "s", "e", " ", "+", ".")
        p[6] += maze.searched / maze.time

        maze = solve.SolveDfs(maze8, "s", "e", " ", "+", ".")
        p[7] += maze.searched / maze.time

        maze = solve.SolveAStar(maze9, "S", "E", " ", "+", ".", verbose=True)
        p[8] += maze.searched / maze.time

    if n != 0:
        [print(f"dfs maze {i+1}", p[i] / n, "nodes/s") for i in range(len(p))]
        print()


def astar_maze_sizes(n):
    p = []
    [p.append(0) for _ in range(9)]
    for _ in range(n):
        maze = solve.SolveAStar(maze1, "S", "E", " ", "#")
        p[0] += maze.searched / maze.time

        maze = solve.SolveAStar(maze2, "S", "E", " ", "#")
        p[1] += maze.searched / maze.time

        maze = solve.SolveAStar(maze3, "S", "E", " ", "#")
        p[2] += maze.searched / maze.time

        maze = solve.SolveAStar(maze4, "S", "E", " ", "#")
        p[3] += maze.searched / maze.time

        maze = solve.SolveAStar(maze5, "S", "E", " ", "#")
        p[4] += maze.searched / maze.time

        maze = solve.SolveAStar(maze6, "s", "e", " ", "+", ".")
        p[5] += maze.searched / maze.time

        maze = solve.SolveAStar(maze7, "s", "e", " ", "+", ".")
        p[6] += maze.searched / maze.time

        maze = solve.SolveAStar(maze8, "s", "e", " ", "+", ".")
        p[7] += maze.searched / maze.time

        maze = solve.SolveAStar(maze9, "S", "E", " ", "+", ".")
        p[8] += maze.searched / maze.time

    if n != 0:
        [print(f"dfs maze {i+1}", p[i] / n, "nodes/s") for i in range(len(p))]
        print()


# time test cases
bfs_maze_sizes(0)
dfs_maze_sizes(0)
astar_maze_sizes(0)

# Drawing the solution to the console
maze = solve.SolveBfs(maze7, "s", "e", " ", "+", ".", verbose=True)
maze.show()
maze = solve.SolveDfs(maze7, "s", "e", " ", "+", ".", verbose=True)
maze.show()
maze = solve.SolveAStar(maze7, "s", "e", " ", "+", ".", verbose=True)
maze.show()

maze = solve.SolveBfs(maze9, "S", "E", " ", "+", ".", verbose=True)
maze.show()
maze = solve.SolveDfs(maze9, "S", "E", " ", "+", ".", verbose=True)
maze.show()
maze = solve.SolveAStar(maze9, "S", "E", " ", "+", ".", verbose=True)
maze.show()
