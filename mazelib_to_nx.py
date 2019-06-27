#!/usr/bin/env python3

import mazelib
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

MAZE_BIGNESS = (3, 3)

class Room():
    pass

maze = mazelib.Prims(*MAZE_BIGNESS).generate()
G = nx.DiGraph()

rooms = np.ndarray(shape=[d - 2 for d in maze.shape], dtype=Room)

for index, room in np.ndenumerate(rooms):
    x = index[0]
    y = index[1]
    x_maze = x + 1
    y_maze = y + 1
    if maze[x_maze, y_maze] == 0:
        rooms[index] = Room()
        x_north = x - 1
        if x_north >= 0 and rooms[(x_north, y)] is not None:
            G.add_edge(rooms[index], rooms[x_north, y], direction='n')
            G.add_edge(rooms[x_north, y], rooms[index], direction='s')
        y_west = y - 1
        if y_west >= 0 and rooms[(x, y_west)] is not None:
            G.add_edge(rooms[index], rooms[x, y_west], direction='w')
            G.add_edge(rooms[x, y_west], rooms[index], direction='e')


print(maze)
nx.draw(G)
plt.show()
