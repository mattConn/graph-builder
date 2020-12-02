import json
import os
import sys
import networkx as nx
import matplotlib.pyplot as plt

filename = 'graph.json' 

if len(sys.argv) < 3:
    print('Missing args')
    sys.exit(1)

# load json
if not os.path.exists(filename):
    f = open(filename,'w')
    f.write(json.dumps(nx.node_link_data(nx.Graph())))
    f.close()

    sys.exit(0)
else:
    with open(filename) as f:
        js_graph = json.load(f)

# make graph from json
graph = nx.readwrite.json_graph.node_link_graph(js_graph)

# read command
cmd = sys.argv[1:]
if cmd[0] == 'addnode': # add node to graph
    graph.add_node(cmd[1])
elif cmd[0] == 'addedge': # add edge
    graph.add_edge(cmd[1],cmd[2])

# write back edits json
f = open(filename,'w')
f.write(json.dumps(nx.node_link_data(graph)))
f.close()

# draw graph
nx.draw_networkx(graph,font_color='black')
plt.savefig('static/graph.png') # save graph image

sys.exit(0)