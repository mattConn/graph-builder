import json
import random
import os
import networkx as nx
from io import BytesIO
import base64
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

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    plt.close()


    return render_template('index.html',
    filepath = filepath % session['filehash'],
    image_base64 = figdata_png,
    matrix = str(nx.to_numpy_array(graph)).replace('.',',').replace('\n',','),
    graph = graph,
    data = json.dumps(nx.node_link_data(graph)) ) 

# add and remove node
@app.route("/addnode")
def addnode():
    def add(graph):
        for i in range(len(graph.nodes)+1):
            if i not in graph.nodes:
                graph.add_node(i)
                break

    updateSessionGraph(add)

    return redirect(url_for('graphInterfaceView'))

@app.route("/removenode")
def removenode():

    def remove(graph):
        if graph.has_node(int(request.args.get('label'))):
            graph.remove_node(int(request.args.get('label')))

    updateSessionGraph(remove)

    return redirect(url_for('graphInterfaceView'))

# add and remove edge 
@app.route("/addedge")
def addedge():
    updateSessionGraph(lambda graph: graph.add_edge(request.args.get('label1'),request.args.get('label2')))

    return redirect(url_for('graphInterfaceView'))

@app.route("/toggleedge")
def toggleedge():

    edge = [int(n) for n in request.args.get('label').split('_')]

    def toggle(graph):
        if graph.has_edge(edge[0],edge[1]):
            graph.remove_edge(edge[0],edge[1])
        else:
            graph.add_edge(edge[0],edge[1])

    updateSessionGraph(toggle)

    return redirect(url_for('graphInterfaceView'))

# complement graph
@app.route("/complement")
def complementgraph():

    graph = getSessionGraph()
    setSessionGraph(nx.complement(graph))

    return redirect(url_for('graphInterfaceView'))

# clear edges 
@app.route("/clearedges")
def clearedges():

    updateSessionGraph(lambda graph: graph.remove_edges_from(graph.edges()))

    return redirect(url_for('graphInterfaceView'))

# clear graph
@app.route("/clear")
def cleargraph():

    updateSessionGraph(lambda graph: graph.clear())

    return redirect(url_for('graphInterfaceView'))


if __name__ == '__main__':
  app.run()
