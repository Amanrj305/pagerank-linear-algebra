import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(edges):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    nx.draw(G, with_labels=True)
    plt.show()
    
    
    
    