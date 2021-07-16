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
	want = [0,1,2,3,4,5]

	graph.add(g)

	assert list(g.nodes) == want, name

def test_empty():
	name = 'empty'
	g = makeGraph(None)
	want = [0]

	graph.add(g)

	assert list(g.nodes) == want, name

def test_deletedNode():
	name = 'deletedNode'
	g = makeGraph(simpleGraph)
	want = [0,1,2,3,4]

	g.remove_node(2)
	graph.add(g)

	assert sorted(list(g.nodes)) == want, name

def test_multipleDeletedNodes():
	name = 'multipleDeletedNodes'
	g = makeGraph(simpleGraph)
	want = [0,1,2,3]

	g.remove_node(2)
	g.remove_node(4)
	graph.add(g)

	assert sorted(list(g.nodes)) == want, name