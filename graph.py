def add(graph):
	for i in range(len(graph.nodes)+1):
		if i not in graph.nodes:
			graph.add_node(i)
			break

def remove(graph,node):
	if graph.has_node(node):
		graph.remove_node(node)