import json
import random
import os
import subprocess
from graphgen import draw, filepath, nx
from flask import Flask, request, render_template, redirect, url_for, session
app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.before_request
def preflight():

    # store empty graph
    if 'graph' not in session:
        session['graph'] = nx.adjacency_data(nx.Graph())

    # remove old graph image
    # if 'filehash' in session and os.path.isfile(filepath % session['filehash']):
    #     os.remove(filepath % session['filehash'])

    # generate new filehash
    session['filehash'] = random.randint(1000,4000)

def getSessionGraph():
    return nx.adjacency_graph(session['graph'])

def setSessionGraph(graph):
    session['graph'] = nx.adjacency_data(graph)

def updateAndDraw():

    if 'graph' not in session:
        session['graph'] = json.dumps( nx.node_link_data(nx.Graph()) )  

    # draw(filepath % session['filehash'])

@app.route("/")
def index():
    graph = getSessionGraph()
    draw(graph, filepath % session['filehash'])

    return render_template('index.html',
    filepath = filepath % session['filehash'],
    matrix = str(nx.to_numpy_array(graph)).replace('.',',').replace('\n',','),
    data = json.dumps(nx.node_link_data(graph)) ) 

# add and remove node
@app.route("/addnode")
def addnode():
    graph = getSessionGraph()
    graph.add_node(request.args.get('label'))
    setSessionGraph(graph)

    return index()

@app.route("/removenode")
def removenode():
    graph = getSessionGraph()

    if graph.has_node(request.args.get('label')):
        graph.remove_node(request.args.get('label'))

    draw(graph, filepath % session['filehash'])
    setSessionGraph(graph)

    return index()

# add and remove edge 
@app.route("/addedge")
def addedge():
    graph = getSessionGraph()
    graph.add_edge(request.args.get('label1'),request.args.get('label2'))
    draw(graph, filepath % session['filehash'])
    setSessionGraph(graph)

    return index()

@app.route("/removeedge")
def removeedge():
    graph = getSessionGraph()

    if graph.has_edge(request.args.get('label1'),request.args.get('label2')):
        graph.remove_edge(request.args.get('label1'),request.args.get('label2'))

    draw(graph, filepath % session['filehash'])
    setSessionGraph(graph)

    return index()

# clear graph
@app.route("/clear")
def cleargraph():
    graph = getSessionGraph()
    graph.clear()
    draw(graph, filepath % session['filehash'])
    setSessionGraph(graph)

    return index()


if __name__ == '__main__':
  app.run()
