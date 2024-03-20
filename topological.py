def robot_traversal(graph, start_node):
    def dfs(node):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
        traversal_order.append(node)

    # Initialize data structures
    visited = {node: False for node in graph}
    traversal_order = []

    # Start DFS from the specified node
    dfs(start_node)

    return traversal_order

# Example usage
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)],
}

start_node = (0, 0)
traversal_order = robot_traversal(graph, start_node)
print("Traverse Order:", traversal_order)
