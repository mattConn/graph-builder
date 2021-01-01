import json
import random
import os
import subprocess
from graphgen import graph, nx
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

def updateAndDraw():
    graph.filehash = random.randint(1000,4000)
    graph.draw(f'static/img/graph{graph.filehash}.png')

@app.route("/")
def index():
    return render_template('index.html',filepath = f'static/img/graph{graph.filehash}.png', data = json.dumps(nx.node_link_data(graph)) ) 

@app.route("/addnode")
def addnode():
    graph.add_node(request.args.get('label'))
    updateAndDraw()
    return redirect(url_for('index'))

@app.route("/addedge")
def addedge():
    graph.add_edge(request.args.get('label1'),request.args.get('label2'))
    updateAndDraw()
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.run()
