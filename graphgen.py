import networkx as nx
import json
import matplotlib.pyplot as plt

# load initial graph
with open('./data.json') as f:
    data = json.load(f)


# make graph from json
graph = nx.DiGraph(nx.readwrite.json_graph.node_link_graph(data))

def draw(filename):
    nx.draw_networkx(graph,font_color='black')
    plt.savefig(filename) # save graph image
    plt.close()



graph.draw = draw
graph.filehash = 0
graph.draw('static/img/graph0.png') # draw initial graph
