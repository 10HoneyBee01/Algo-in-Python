from collections import deque

def is_valid_move(x, y, grid):
    # Check if the move is within the grid boundaries and not on an obstacle
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X':
        return True
    return False

def find_path_with_obstacles(grid, start, goal):
    # Define possible movements: up, down, left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Create a queue for BFS
    queue = deque([(start, [])])
    
    # Create a set to track visited cells
    visited = set()
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == goal:
            return path + [(x, y)]
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, grid):
                queue.append(((new_x, new_y), path + [(x, y)]))
    
    return None  # No path found
grid = [
    ['X', 'X', ' ', 'X', ' '],
    ['X', ' ', ' ', ' ', ' '],
    ['X', ' ', 'X', 'X', ' '],
    [' ', ' ', 'X', ' ', ' '],
    [' ', 'X', 'X', 'X', ' ']
]

start = (0, 2)
goal = (4, 4)

path = find_path_with_obstacles(grid, start, goal)

if path:
    print("Path found from start to goal:")
    for x, y in path:
        print(f"({x}, {y})")
else:
    print("No path found.")
