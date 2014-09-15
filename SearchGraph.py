import sys

# SearchGraph.py
#
# Implementation of iterative deepening search for use in finding optimal routes
# between locations in a graph. In the graph to be searched, nodes have names
# (e.g. city names for a map).
#
# An undirected graph passed in as a text file (first command line argument). 
#
# Usage: python SearchGraph.py graphFile startLocation endLocation
# 
# Author: Richard Zanibbi, RIT, Nov. 2011
def read_graph(filename): 
	"""Read in edges of a graph represented one per line,
	using the format: srcStateName destStateName""" 
	print("Loading graph: " + filename) 
	edges = {}

	inFile = open(filename)
	for line in inFile:
		roadInfo = line.split()

		# Skip blank lines, read in contents from non-empty lines.
		if (len(roadInfo) > 0):
			srcCity = roadInfo[0]
			destCity = roadInfo[1]

			if srcCity in edges:
				edges[srcCity] = edges[srcCity] + [destCity ]
			else:
				edges[srcCity] = [ destCity ] 

			if destCity in edges:
				edges[destCity] = edges[destCity] + [ srcCity ]
			else:
				edges[destCity] = [ srcCity ]
	return edges

######################################
# Add functions for search, output
# etc. here
######################################

# TBD

#########################
# Main program
#########################
def main():
	if len(sys.argv) != 4:
		print('Usage: python SearchGraph.py graphFilename startNode goalNode')
		return 
	else:
		# Create a dictionary (i.e. associative array, implemented as a hash table)
		# for edges in the map file. Read it in, get start and end nodes for the
		# search. Each entry is a string for the location, and a list of strings
		# for the adjacent locations (cities) in the state space.
		edges = {}
		edges = read_graph(sys.argv[1])
		start = sys.argv[2]
		goal = sys.argv[3]

		# Comment out the following lines to hide the graph description.
		print("-- Edge List (Edge Dictionary Data) ------------------------")
		for location in edges.keys():
			s = '  ' + location + ':\n     '
			s = s + str(edges[location])
			print(s)
						
		if not start in edges.keys():
			print("Start location is not in the graph.")
		else:
			print('')
			print('-- States Visited ----------------')
			print('TBD')  # program will need to show the search tree.
			print('')
			print('--  Solution for: ' + start + ' to ' + goal + '-------------------')
			print('TBD') # program will need to provide solution path or indicate failure.

# Execute the main program.
main()

