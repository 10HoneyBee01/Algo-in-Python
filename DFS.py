def is_valid_move(x, y, grid):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X':
        return True
    return False

def find_path_with_obstacles(grid, start, goal, visited):
    x, y = start

    if (x, y) == goal:
        return [start]

    visited.add((x, y))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, grid) and (new_x, new_y) not in visited:
            path = find_path_with_obstacles(grid, (new_x, new_y), goal, visited)
            if path:
                return [start] + path

    return None
grid = [
    ['X', 'X', ' ', 'X', ' '],
    ['X', ' ', ' ', ' ', ' '],
    ['X', ' ', 'X', 'X', ' '],
    [' ', ' ', 'X', ' ', ' '],
    [' ', 'X', 'X', 'X', ' ']
]

start = (0, 2)
goal = (4, 4)
visited = set()

path = find_path_with_obstacles(grid, start, goal, visited)

if path:
    print("Path found from start to goal:")
    for x, y in path:
        print(f"({x}, {y})")
else:
    print("No path found.")
