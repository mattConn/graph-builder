import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

def draw(filename):
    nx.draw_networkx(graph,font_color='black')
    plt.savefig(filename) # save graph image
    plt.close()

graph.draw = draw
graph.filehash = 0
