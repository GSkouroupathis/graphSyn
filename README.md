graphSyn - graph algorithms in one place
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Import graph.py to your project
2) Create a new Graph
3) Apply its algorithms
~~~~~~~~~~~~~

~~~~
Function List:
1) add_node(name): Adds a node to the graph
2) add_edge(weight, f_node_name, s_node_name, both): Adds an edge to the graph. 'both' means the edge travles both ways
all_paths(f_node, l_node): Returns all paths from f_node to l_node
3) lazy_shortest_path(f_node, l_node): Returns the shortest path from f_node to l_node (Lazy)
4) lazy_longest_path(f_node, l_node): Returns the longest path from f_node to l_node (Lazy)
5) prim(): Runs Prim's algorithm to return the minimum spanning tree of the graph
	Graph has to be connected
	Also all edges need to connect nodes in both directions
6)dijkstra(s_node, f_node): Runs Dijkstra's algorithm to return shortest path from s_node to f_node and the distance
7)alphastar(s_node, f_node, attr): Runs A* algorithm to return shortest path from s_node to f_node and the distance
	Uses attr as the attribute with which it computers the A* Heuristic
	Warning: Since this algorithm is used in AI, make sure your graph doesn't contain any loops
	Returns None if no available path
~~~~
See 'test.py' and 'test1.py' for examples
