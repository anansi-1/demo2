import heapq
import time
grid = [
    ['S', 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 'G']
]
# locating the start and goal 
def find_positions(grid):
    start = goal = None
    for i, r in enumerate(grid):
        for j, val in enumerate(r):
            if val == 'S':
                start = (i, j)
            elif val == 'G':
                goal = (i, j)
    return start, goal

start, goal = find_positions(grid)
# Manhattan Distance Heuristic
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
# Valid Neighbors 
def get_neighbors(pos, grid):
    x, y = pos
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            neighbors.append((nx, ny))
    return neighbors
# Greedy Best-First Search
def greedy_search(grid, start, goal):
    open_list = [(manhattan(start, goal), start)]
    came_from = {start: None}
    visited = set()
    nodes_expanded = 0
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            break
        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited and neighbor not in came_from:
                heapq.heappush(open_list, (manhattan(neighbor, goal), neighbor))
                came_from[neighbor] = current
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, nodes_expanded
# A* Search Algorith
def a_star_search(grid, start, goal):
    open_list = [(manhattan(start, goal), 0, start)]
    came_from = {start: None}
    g_cost = {start: 0}
    visited = set()
    nodes_expanded = 0

    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current == goal:
            break
        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1
        for neighbor in get_neighbors(current, grid):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + manhattan(neighbor, goal)
                heapq.heappush(open_list, (f, new_g, neighbor))
                came_from[neighbor] = current
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, nodes_expanded
# Run and Compare the algorithms 
t0 = time.time()
greedy_path, greedy_nodes = greedy_search(grid, start, goal)
greedy_time = time.time() - t0

t1 = time.time()
astar_path, astar_nodes = a_star_search(grid, start, goal)
astar_time = time.time() - t1

print("Greedy Best-First Search:")
print("Path:", greedy_path)
print("Nodes Expanded:", greedy_nodes)
print("Time Taken:", round(greedy_time, 6), "seconds")

print("\nA* Search:")
print("Path:", astar_path)
print("Nodes Expanded:", astar_nodes)
print("Time Taken:", round(astar_time, 6), "seconds")

# Check for optimality
print("\nOptimality Check:")
if len(greedy_path) == len(astar_path):
    print("Both algorithms found the optimal path.")
else:
    print("A* found a better (shorter) path.")

bonus challenge 

========== Greedy Best-First Search & A* with Graph Search and Euclidean Distance ==========
import heapq
import time
import math
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
def get_neighbors(pos, grid):
    x, y = pos
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    return [ (x+dx, y+dy) for dx, dy in directions 
             if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] != 1 ]
def find_positions(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 'S': start = (i, j)
            if val == 'G': goal = (i, j)
    return start, goal
def greedy_search(grid):
    start, goal = find_positions(grid)
    open_list = [(euclidean(start, goal), start)]
    came_from = {start: None}
    visited = set()
    nodes_expanded = 0
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal: break
        if current in visited: continue
        visited.add(current)
        nodes_expanded += 1
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited and neighbor not in came_from:
                heapq.heappush(open_list, (euclidean(neighbor, goal), neighbor))
                came_from[neighbor] = current
    path, node = [], goal
    while node: path.append(node); node = came_from.get(node)
    path.reverse()
    return path, nodes_expanded
def a_star_search(grid):
    start, goal = find_positions(grid)
    open_list = [(euclidean(start, goal), 0, start)]
    came_from = {start: None}
    g_cost = {start: 0}
    visited = set()
    nodes_expanded = 0
    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current == goal: break
        if current in visited: continue
        visited.add(current)
        nodes_expanded += 1
        for neighbor in get_neighbors(current, grid):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + euclidean(neighbor, goal)
                heapq.heappush(open_list, (f, new_g, neighbor))
                came_from[neighbor] = current
    path, node = [], goal
    while node: path.append(node); node = came_from.get(node)
    path.reverse()
    return path, nodes_expanded
# Define grid
grid = [
    ['S', 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 'G']
]

# Run Greedy with Euclidean
start_time = time.time()
g_path, g_expanded = greedy_search(grid)
g_time = time.time() - start_time
print("Greedy Best-First Search with Euclidean Distance")
print("Path:", g_path)
print("Nodes Expanded:", g_expanded)
print("Time Taken:", round(g_time, 6), "seconds")

# Run A* with Euclidean
start_time = time.time()
a_path, a_expanded = a_star_search(grid)
a_time = time.time() - start_time
print("\nA* Search with Euclidean Distance")
print("Path:", a_path)
print("Nodes Expanded:", a_expanded)
print("Time Taken:", round(a_time, 6), "seconds")