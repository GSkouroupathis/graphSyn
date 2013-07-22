graphSyn - graph algorithms in one place
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1) Import graph.py to your project
2) Create a new Graph
3) Apply its algorithms

Function List:
~~~~~~~~~~~~~
add_node(name): Adds a node to the graph
add_edge(weight, f_node_name, s_node_name, both): Adds an edge to the graph. 'both' means the edge travles both ways
all_paths(f_node, l_node): Returns all paths from f_node to l_node
lazy_shortest_path(f_node, l_node): Returns the shortest path from f_node to l_node (Lazy)
lazy_longest_path(f_node, l_node): Returns the longest path from f_node to l_node (Lazy)
prim(): Runs Prim's algorithm to return the minimum spanning tree of the graph
	Graph has to be connected
	Also all edges need to connect nodes in both directions
dijkstra(s_node, f_node): Runs Dijkstra's algorithm to return shortest path from s_node to f_node and the distance

See 'test.py' for examples
