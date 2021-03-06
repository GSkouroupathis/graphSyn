from node import Node
from edge import Edge
import random

class Graph(object):
	
	#Class constructor
	def __init__(self, name):
		self.name = name
		self.nodes = {}
		self.edges = []
		self.graph = {}
		self.MAX_DIST = 9999999999999
	
	#Adds a node to the graph
	def add_node(self, name):
		if name not in self.nodes.keys():
			n = Node(name)
			self.nodes[name] = n
			self.graph[name] = []
			return True
		else: return "Node", name, "already exists"
	
	#Adds an edge to the graph
	def add_edge(self, weight, f_node_name, s_node_name, both):
		if f_node_name not in self.nodes.keys(): return f_node_name + " not a valid node"
		if s_node_name not in self.nodes.keys(): return s_node_name + " not a valid node"
		e = Edge(weight)
		self.edges.append(e)
		self.graph[f_node_name].append( (s_node_name, weight) )
		if both:
			e = Edge(weight)
			self.edges.append(e)
			self.graph[s_node_name].append( (f_node_name, weight) )
		return True
	
	#Returns all paths from f_node to l_node
	def all_paths(self, f_node, l_node, path = [], pathWeight = 0):
		path += [f_node]
		
		if f_node == l_node:
			return [ (path, pathWeight) ]
		
		allPaths = []
		
		for (n_node, weight) in self.graph[f_node]:
			path2=path[:] #stupid thing because lists are mutable
			if n_node not in path:
				newPaths = self.all_paths(n_node, l_node, path2, pathWeight + weight)
				for newPath in newPaths:
					allPaths.append(newPath)
		
		return allPaths
	
	#Returns the shortest path from f_node to l_node (Lazy)
	def lazy_shortest_path(self, f_node, l_node):
		return reduce(lambda f_path, s_path: f_path if f_path[1]<s_path[1] else s_path, self.all_paths(f_node, l_node, [], 0))
	
	#Returns the longest path from f_node to l_node (Lazy)
	def lazy_longest_path(self, f_node, l_node):
		return reduce(lambda f_path, s_path: f_path if f_path[1]>s_path[1] else s_path, self.all_paths(f_node, l_node, [], 0))
	
	#Runs Prim's algorithm to return the minimum spanning tree of the graph
	#Graph has to be connected
	#Also all edges need to connect nodes in both directions
	#Max distance = self.MAX_DIST
	def prim(self):
		prim_graph = {}
		new_node = random.choice( self.graph.keys() )
		prim_graph[new_node] = []
		print "init"
		print prim_graph
		while sorted(prim_graph.keys()) != sorted(self.graph.keys()):

			least_weight = self.MAX_DIST + 1
			new_connection = None
			for node in prim_graph.keys():
				for nodedge in [x for x in self.graph[node] if x[0] not in prim_graph.keys()]:
					if nodedge[1] < least_weight:
						new_connection = (node, nodedge[0], nodedge[1])
						least_weight = nodedge[1]

			prim_graph[new_connection[0]].append( (new_connection[1], new_connection[2]) )
			prim_graph[new_connection[1]] = [ (new_connection[0], new_connection[2]) ]
					
		return prim_graph
	
	#Runs Dijkstra's algorithm to return shortest path from s_node to f_node
	#and the distance
	#Max distance = self.MAX_DIST
	def dijkstra(self, s_node, f_node):
		dijkstra_path = []
		nodes_visited = [s_node]
		
		#create the vertices/shortest dist from s_node table
		nodes_sdist = {}
		for i in self.graph.keys():
			nodes_sdist[i] = [self.MAX_DIST, None]
		nodes_sdist[s_node][0] = 0 #{s_node: [0, None]}
		
		#construct candidate nodes
		while f_node not in nodes_visited:
			candidate_nodes = []
			for node in nodes_visited:
				for (neighbour_node, dist) in self.graph[node]:
					if neighbour_node not in nodes_visited:
						new_dist = nodes_sdist[node][0] + dist
						if new_dist < nodes_sdist[neighbour_node][0]:
							nodes_sdist[neighbour_node] = (new_dist, node)
							candidate_nodes.append( (neighbour_node, new_dist) )
						else:
							candidate_nodes.append( (neighbour_node, nodes_sdist[neighbour_node][0]) )
			nodes_visited.append( sorted(candidate_nodes, key=lambda x: x[1])[0][0] )
			
		#traverse graph in reverse direction to find dijkstra_path
		#while s_node not in dijkstra_path:
		distance = nodes_sdist[f_node][0]
		dijkstra_path.append(f_node)
		i=f_node
		while s_node not in dijkstra_path:
			j = nodes_sdist[i][1]
			dijkstra_path.append( j )
			i = j
				
		return (dijkstra_path[::-1], distance)
	
	#Runs A* algorithm to return shortest path from s_node to f_node
	#and the distance
	#Uses attr as the attribute with which it computers the A* Heuristic
	#Warning: Since this algorithm is used in AI, make sure your graph doesn't
	#contain any loops
	#Returns None if no available path
	def aplhastar(self, s_node, f_node, attr):
		if s_node not in self.graph.keys() or f_node not in self.graph.keys(): return None
		fbuDic = {} #Found but Unexpanded Nodes Dictionary
		
		if s_node == f_node: return ([s_node], 0)
		
		fbuDic[(s_node,)] = (0, self.nodes[s_node].attrs[attr]) #path : (distance, heuristic)
		
		while True: 
			smallestPath = sorted(fbuDic.keys(), key=lambda x: fbuDic[x][1])[0] #sort paths according to heuristic
			smallestNode = smallestPath[-1]
			smallestDist = fbuDic[smallestPath][0]
			if smallestNode == f_node: return (list(smallestPath), smallestDist)
			
			#Add neighbours to fbuDic
			for (nn, nndistance) in self.graph[smallestNode]:
				fbuDic[smallestPath+(nn,)] = (smallestDist+nndistance, smallestDist+nndistance+self.nodes[nn].attrs[attr])
			del fbuDic[smallestPath]
			if fbuDic == {}: return None
				
	#Class representation
	def __repr__(self):
		return self.name + ": " + str(self.graph)
		
		
		
		
		
		
		
		
		
		
		
		
	
