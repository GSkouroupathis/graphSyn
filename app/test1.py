from graph import *
import random

g = Graph("my graph")
dic1 = {'Arad':300, 'Timisoara':320, 'Sibiu':250, 'Oradea':380,
		'Lugoj':240, 'Rimnicu':190, 'Oradea':380, 'Fagaras':170,
		'Nicosia':0}
for city in dic1:
	g.add_node(city)
	g.nodes[city].attrs['weight'] = dic1[city]

g.add_edge(100, 'Arad', 'Timisoara', False)
g.add_edge(140, 'Arad', 'Sibiu', False)
g.add_edge(70, 'Arad', 'Zerind', False)
g.add_edge(100, 'Timisoara', 'Lugoj', False)
g.add_edge(80, 'Sibiu', 'Rimnicu', False)
g.add_edge(150, 'Sibiu', 'Oradea', False)
g.add_edge(100, 'Sibiu', 'Fagaras', False)
g.add_edge(200, 'Zerind', 'Nicosia', False)

print "GRAPH"
print g
print
for n in g.graph:
	print n, g.nodes[n].attrs['weight']
print
print g.aplhastar('Arad', 'Nicosia', 'weight')
