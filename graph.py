def add(graph):
	for i in range(len(graph.nodes)+1):
		if i not in graph.nodes:
			graph.add_node(i)
			break

def remove(graph,node):
	if graph.has_node(node):
		graph.remove_node(node)

def toggle(graph,edge):
	if len(edge) != 2 or edge[0] == edge[1]: return 

	if graph.has_edge(edge[0],edge[1]):
		graph.remove_edge(edge[0],edge[1])
	else:
		graph.add_edge(edge[0],edge[1])