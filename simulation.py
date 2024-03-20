import networkx as nx
import matplotlib.pyplot as plt
import pyautogui
# Create a sample graph
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10)]
G.add_edges_from(edges)

# Function to visualize DFS
def visualize_dfs(graph, start_node):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 5))

    visited_nodes = set()
    stack = [start_node]
    step = 1  # Initialize step counter
    while stack:
        node = stack.pop()
        visited_nodes.add(node)
        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_color=['lightgreen' if n in visited_nodes else 'lightblue' for n in G.nodes()],
            node_size=500,
            font_size=10,
            font_color='black',
            font_weight='bold'
        )
        plt.title(f"DFS: Visited Node {node}")

        plt.show(block=False)
        plt.pause(0.5)
        plt.clf()

        for neighbor in graph.neighbors(node):
            if neighbor not in visited_nodes and neighbor not in stack:
                stack.append(neighbor)        
        # Save screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save(f"dfs_step_{step}.png")
        step += 1
#Function ends here !!!!
visualize_dfs(G, 1)
plt.show()
