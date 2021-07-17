import networkx as nx
import graph

simpleGraph = {
	0: [1,2],
	1: [0,3,4],
	2: [0],
	3: [1,4],
	4: [1,3]
}

edgelessGraph = {
	0: [],
	1: [],
	2: []
}

def makeGraph(edgeList):
	return nx.Graph(edgeList)

def sortedPairList(pairList):
	return sorted([tuple(sorted(pair)) for pair in pairList])

def test_populated():
	name = 'populated'
	g = makeGraph(simpleGraph)
	want = [(0, 3), (0, 4), (1, 3), (1, 4), (3, 4)]

	graph.complement(g,0)

	assert sortedPairList(g.edges) == want, name

def test_complementTwice():
	name = 'complementTwice'
	g = makeGraph(simpleGraph)
	want = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]

	graph.complement(g,0)
	graph.complement(g,0)

	assert sortedPairList(g.edges) == want, name

def test_empty():
	name = 'empty'
	g = makeGraph(None)
	want = []

	# no-op
	graph.complement(g,0)

	assert sortedPairList(g.edges) == want, name

def test_noEdges():
	name = 'noEdges'
	g = makeGraph(edgelessGraph)
	want = [(0, 1), (0, 2)]

	graph.complement(g,0)

	assert sortedPairList(g.edges) == want, name

def test_badNode():
	name = 'badNode'
	g = makeGraph(simpleGraph)
	want = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]

	# no-op
	graph.complement(g,6)

	assert sortedPairList(g.edges) == want, name