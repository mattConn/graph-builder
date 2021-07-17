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

def sortedPairList(pairList):
	return sorted([tuple(sorted(pair)) for pair in pairList])

def test_populated():
	name = 'populated'
	g = makeGraph(simpleGraph)
	want = [(0, 1), (0, 2), (1, 4), (3, 4)]

	graph.toggle(g,[1,3])

	assert sortedPairList(g.edges) == want, name

def test_toggleTwice():
	name = 'toggleTwice'
	g = makeGraph(simpleGraph)
	want = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]

	graph.toggle(g,[1,3])
	graph.toggle(g,[1,3])

	assert sortedPairList(g.edges) == want, name

def test_empty():
	name = 'empty'
	g = makeGraph(None)
	want = [(0,1)]

	graph.toggle(g,[0,1])

	assert sortedPairList(g.edges) == want, name

def test_newNodes():
	name = 'newNodes'
	g = makeGraph(simpleGraph)
	want = [0,1,2,3,4,5,6]

	graph.toggle(g,[5,6])

	assert list(g.nodes) == want, name

def test_badEdge():
	name = 'badEdge'
	g = makeGraph(simpleGraph)
	want = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]

	# effectively a no-op
	graph.toggle(g,[5])

	assert sortedPairList(g.edges) == want, name

def test_selfEdge():
	name = 'selfEdge'
	g = makeGraph(simpleGraph)
	want = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]

	# effectively a no-op
	graph.toggle(g,[3,3])

	assert sortedPairList(g.edges) == want, name