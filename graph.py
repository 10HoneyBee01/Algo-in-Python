import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph

nodes = [1,2,3,4,5,6,7,8,9]
G.add_nodes_from(nodes)

# Add edges to the graph
edges = [(1,2), (1,3), (2,4), (2,5), (3,6), (3,7), (4,8),(4,9),(5,10)]
G.add_edges_from(edges)

# Visualize the graph
pos = nx.spring_layout(G)  # Positioning the nodes
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', font_weight='bold')
plt.title('Sample Graph')
plt.show()
