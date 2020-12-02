import json
import random
import os
import subprocess
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html') 

@app.route("/addnode")
def addnode():
    subprocess.call(['python', 'graphbuilder.py', 'addnode', request.args.get('label')])
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.run()