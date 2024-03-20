class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                if node in self.graph:
                    stack.extend([neighbor for neighbor in self.graph[node] if neighbor not in visited])

    def dfs_from_every_node(self):
        for node in self.graph:
            print(f"DFS traversal starting from node {node}: ", end='')
            self.dfs(node)
            print()

# Create a sample graph with 10 nodes and edges
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)
g.add_edge(4, 8)
g.add_edge(4, 9)
g.add_edge(5, 10)

# Perform DFS from every node
g.dfs_from_every_node()
