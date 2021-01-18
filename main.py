import json
import random
import os
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, redirect, url_for, session
app = Flask(__name__)

app.secret_key = os.urandom(24)

filepath = 'static/img/graph%s.png'

def getSessionGraph():
    return nx.adjacency_graph(session['graph'])

def setSessionGraph(graph):
    session['graph'] = nx.adjacency_data(graph)

def updateSessionGraph(update = lambda _: None):
    graph = getSessionGraph()
    update(graph)
    setSessionGraph(graph)

@app.before_request
def before_request():
    # store empty graph
    if 'graph' not in session:
        session['graph'] = nx.adjacency_data(nx.Graph())

@app.route("/")
def graphInterfaceView():
    # remove old graph image
    if 'filehash' in session and os.path.isfile(filepath % session['filehash']):
        os.remove(filepath % session['filehash'])

    # generate new filehash
    session['filehash'] = random.randint(1000,4000)

    graph = getSessionGraph()

    nx.draw_networkx(graph,font_color='white', pos=nx.circular_layout(graph))
    plt.savefig(filepath % session['filehash']) # save graph image
    plt.close()


    return render_template('index.html',
    filepath = filepath % session['filehash'],
    matrix = str(nx.to_numpy_array(graph)).replace('.',',').replace('\n',','),
    data = json.dumps(nx.node_link_data(graph)) ) 

# add and remove node
@app.route("/addnode")
def addnode():
    updateSessionGraph(lambda graph: graph.add_node(request.args.get('label')))

    return graphInterfaceView()

@app.route("/removenode")
def removenode():

    def remove(graph):
        if graph.has_node(request.args.get('label')):
            graph.remove_node(request.args.get('label'))

    updateSessionGraph(remove)

    return graphInterfaceView()

# add and remove edge 
@app.route("/addedge")
def addedge():
    updateSessionGraph(lambda graph: graph.add_edge(request.args.get('label1'),request.args.get('label2')))

    return graphInterfaceView()

@app.route("/removeedge")
def removeedge():

    def remove(graph):
        if graph.has_edge(request.args.get('label1'),request.args.get('label2')):
            graph.remove_edge(request.args.get('label1'),request.args.get('label2'))

    updateSessionGraph(remove)

    return graphInterfaceView()

# clear graph
@app.route("/clear")
def cleargraph():

    updateSessionGraph(lambda graph: graph.clear())

    return graphInterfaceView()


if __name__ == '__main__':
  app.run()
