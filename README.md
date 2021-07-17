# Graph Builder

This is a Flask webapp that interfaces with a NetworkX graph object.

## Features

- Add/remove edges and nodes via adjacency matrix interface
- Complement graph/single node
- Clear edges/entire graph
- Display graph projection PNG 
- Display adjacency matrix data for NumPy array
- Display JSON data for D3.js

## Usage
Run `python main.py`. The adjacency matrix interface is used as follows:

- \+ to add node
- Click node in table header to remove it
- Click cell to toggle edge
- ~ to toggle all edges for a node
- ~E to toggle all edges
- E=0 to remove all edges
- V=0 to remove all nodes

## Testing
Run `pytest` or `python -m pytest` to test:
- node insertion
- node deletion
- edge complement
- complement all edges for node 