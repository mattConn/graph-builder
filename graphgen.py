import networkx as nx
import json
import matplotlib.pyplot as plt


graph = nx.Graph()

def draw(filename):
    nx.draw_networkx(graph,font_color='black', pos=nx.circular_layout(graph))
    plt.savefig(filename) # save graph image
    plt.close()



graph.draw = draw
graph.filehash = 0
graph.draw('static/img/graph0.png') # draw initial graph
