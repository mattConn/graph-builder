import networkx as nx
import json
import matplotlib.pyplot as plt


graph = nx.Graph()

def draw(filename):
    nx.draw_networkx(graph,font_color='black', pos=nx.circular_layout(graph))
    plt.savefig(filename) # save graph image
    plt.close()

filepath = 'static/img/graph%s.png'

draw('static/img/graph0.png') # draw initial graph
