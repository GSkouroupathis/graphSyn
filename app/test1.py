from graph import *
import random
#
g = Graph("my graph")
dic1 = {'Arad':366, 'Timisoara':329, 'Sibiu':253, 'Oradea':380,
		'Lugoj':244, 'Rimnicu':193, 'Fagaras':178, 'Mehadia':241,
		'Craiova':160, 'Pitesti':98, 'Zerind':374, 'Bucharest':0}

for city in dic1:
	g.add_node(city)
	g.nodes[city].attrs['weight'] = dic1[city]

g.add_edge(118, 'Arad', 'Timisoara', False)
g.add_edge(140, 'Arad', 'Sibiu', False)
g.add_edge(75, 'Arad', 'Zerind', False)
g.add_edge(111, 'Timisoara', 'Lugoj', False)
g.add_edge(80, 'Sibiu', 'Rimnicu', False)
g.add_edge(151, 'Sibiu', 'Oradea', False)
g.add_edge(99, 'Sibiu', 'Fagaras', False)
g.add_edge(71, 'Zerind', 'Oradea', False)
g.add_edge(70, 'Lugoj', 'Mehadia', False)
g.add_edge(146, 'Rimnicu', 'Craiova', False)
g.add_edge(97, 'Rimnicu', 'Pitesti', False)
g.add_edge(71, 'Oradea', 'Zerind', False)
g.add_edge(211, 'Fagaras', 'Bucharest', False)
g.add_edge(151, 'Oradea', 'Sibiu', False)

print "GRAPH"
print g
print
for n in g.graph:
	print n, g.nodes[n].attrs['weight']
print
print g.aplhastar('Arad', 'Bucharest', 'weight')
