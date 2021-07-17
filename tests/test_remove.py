import networkx as nx
import graph

simpleGraph = {
	0: [1,2],
	1: [0,3,4],
	2: [0],
	3: [1,4],
	4: [1,3]
}

def makeGraph(edgeList):
	return nx.Graph(edgeList)

def test_populated():
	name = 'populated'
	g = makeGraph(simpleGraph)
	want = [0,1,2,4]

	graph.remove(g,3)

	assert list(g.nodes) == want, name

def test_empty():
	name = 'empty'
	g = makeGraph(None)
	want = []

	# effectiveley a no-op
	graph.remove(g,3)

	assert list(g.nodes) == want, name

def test_singleton():
	name = 'singleton'
	g = makeGraph({0: []})
	want = []

	graph.remove(g,0)

	assert list(g.nodes) == want, name