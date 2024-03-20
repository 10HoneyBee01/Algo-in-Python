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

print("DFS traversal starting from node 1:")
g.dfs(1)
print()
print("DFS traversal starting from node 2:")
g.dfs(2)
print()
print("DFS traversal starting from node 3:")
g.dfs(3)
print()
print("DFS traversal starting from node 4:")
g.dfs(4)
print()
print("DFS traversal starting from node 5:")
g.dfs(5)
print()
print("DFS traversal starting from node 6:")
g.dfs(6)
print()
print("DFS traversal starting from node 7:")
g.dfs(7)
print()
print("DFS traversal starting from node 8:")
g.dfs(8)
print()
print("DFS traversal starting from node 9:")
g.dfs(9)
print()
print("DFS traversal starting from node 10:")
g.dfs(10)