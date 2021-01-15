import json
import random
import os
import subprocess
from graphgen import graph, draw, filepath, nx
from flask import Flask, request, render_template, redirect, url_for, session
app = Flask(__name__)

app.secret_key = os.urandom(24)

def updateAndDraw():
    if 'filehash' in session and os.path.isfile(filepath % session['filehash']): # clean up
        os.remove(filepath % session['filehash'])

    session['filehash'] = random.randint(1000,4000)
    draw(filepath % session['filehash'])

@app.route("/")
def index():
    updateAndDraw()
    return render_template('index.html',filepath = filepath % session['filehash'], data = json.dumps(nx.node_link_data(graph)) ) 

# add and remove node
@app.route("/addnode")
def addnode():
    graph.add_node(request.args.get('label'))
    return index()

@app.route("/removenode")
def removenode():
    if graph.has_node(request.args.get('label')):
        graph.remove_node(request.args.get('label'))
    return index()

# add and remove edge 
@app.route("/addedge")
def addedge():
    graph.add_edge(request.args.get('label1'),request.args.get('label2'))
    return index()

@app.route("/removeedge")
def removeedge():
    if graph.has_edge(request.args.get('label1'),request.args.get('label2')):
        graph.remove_edge(request.args.get('label1'),request.args.get('label2'))
    return index()

# clear graph
@app.route("/clear")
def cleargraph():
    graph.clear()
    return index()


if __name__ == '__main__':
  app.run()
