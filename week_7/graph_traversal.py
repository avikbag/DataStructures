import operator
import sys

def dfs(graph, root):
	stack = [root]
	visited = [root]

	while stack:
		node = stack[-1]
		edges = graph.get(node)
		next = 0
		
		for x in edges:
			if x not in visited:
				stack.append(x)
				visited.append(x)
				next = 1
				break
		if next == 0:
			stack.pop()

	return visited

def bfs(graph, root):
	queue = [root]
	visited = [root]

	while queue:
		node = queue[0]
		edges = graph.get(node)
		
		for x in edges:
			if x not in visited:
				queue.append(x)
				visited.append(x)
		queue.pop(0)

	return visited

def main():
	graph = {	'A': list(['B', 'C', 'D']),
         		'B': list(['A', 'E', 'F']),
		        'C': list(['A', 'G']),
		        'D': list(['A', 'E', 'G', 'H']),
		        'E': list(['B', 'D', 'I']),
		        'F': list(['B', 'H']),
		        'G': list(['C', 'D']),
		        'H': list(['D', 'F']),
		        'I': list(['E'])}

	sorted_x = sorted(graph.items(), key=operator.itemgetter(0))
	print "Adjacency list for the graph used"
	for x in sorted_x:
		print x[0],
		print " -> ",
		print x[1]

	dfs_trav = dfs(graph, 'D')
 	print "DFS on the given graph (root = Node D)"
 	for x in dfs_trav:
 		print "-> %s "%x,
 	print "\n",

 	bfs_trav = bfs(graph, 'D')
 	print "BFS on the given graph (root = Node D)"
 	for x in bfs_trav:
 		print "-> %s "%x,
 	print "\n",

if __name__ == "__main__":
	main()
