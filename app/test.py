from graph import *
import random, time

g = Graph("my graph")
for i in ['A','B','C','D', 'E']:
	g.add_node(i)

g.add_edge(1, 'A', 'C', True)
g.add_edge(2, 'A', 'B', True)
g.add_edge(3, 'B', 'D', True)
g.add_edge(4, 'A', 'D', True)
g.add_edge(5, 'B', 'E', True)
g.add_edge(6, 'A', 'E', True)
g.add_edge(7, 'E', 'D', True)

print "GRAPH"
print g
print "LAZY"
g.lazy_shortest_path('C', 'E')
print "DIJKSTRA"
print g.dijkstra('C', 'E')
