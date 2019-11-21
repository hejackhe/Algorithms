import itertools
from collections import defaultdict

class Maze:
	def __init__(self):
		self.height = 0
		self.width = 0
		self.special_coords = []
		self.maze_coords = []
		self.maze_walls = []
		self.maze_open_areas = []
		self.maze_graph = defaultdict(list)
		pass

	def addCoordinate(self,x,y,blockType):
		"""
		Add information about a coordinate on the maze grid
		x is the x coordinate
		y is the y coordinate
		blockType: 0 for an open space and 1 for a wall
		"""
	# at each call of this method, it also updates the Maze's maximum height and width
		if x >= 0 and y >= 0:
			if y > self.height:
				self.height = y
			if x > self.width:
				self.width = x
			self.special_coords.append((x, y, blockType))
		else:
			print("Error: x and y values cannot be negative.")
		pass

	def printMaze(self):
		"""
		Prints out an ascii representation of the maze.
		A * indicates a wall and a empty space indicates an open space in the maze
		"""
		for i in range(self.height + 1):
			row = ''
			# i_columns collects all tuples from added coordinates that have i for their y coordinate
			i_columns = [tup for tup in self.special_coords if tup[1] == i]
			# sorted_columns orders i_columns according to their x coordinates in reverse order (for use as a stack)
			sorted_columns = sorted(i_columns, key=lambda tup: tup[0], reverse=True)
			for x in range(self.width + 1):
				# creates a wall at this coordinate if no special treatment specified by addCoordinate()
				if x not in [tup[0] for tup in sorted_columns]:
					row += '*'
					self.maze_coords.append((x,i,1))
				# checks stack if blocktype of special coordinate should be an open area (uses stack ADT to preserve order in x coordinates for row y)
				elif sorted_columns.pop()[2] == 0:    # if x is not one of the special coord's x then that x must be the referring 
					row += ' '                        # to the first popped tuple in the reverse ordered list of special coords
					self.maze_coords.append((x,i,0))
				else:
					row += '*'
					self.maze_coords.append((x,i,1))
			# once row i is processed, print row (this preserves ordering of y coordinates)
			print(row)
		# updates class' maze_walls and maze_open_areas with updated coordinates for use in other functions
		self.maze_walls = [(coord[0],coord[1]) for coord in self.maze_coords if coord[2]==1]
		self.maze_open_areas = [(coord[0],coord[1]) for coord in self.maze_coords if coord[2]==0]
		pass
	
	# creates adjacency list representing graph of open areas in maze
	def createMazeGraph(self):
		for (x, y) in self.maze_open_areas:
			self.maze_graph[(x, y)]
			for coord in self.maze_open_areas:
				if x == coord[0] + 1 and y == coord[1]:
					self.maze_graph[(x, y)].append(coord)
				elif x == coord[0] - 1 and y == coord[1]:
					self.maze_graph[(x, y)].append(coord)
				elif x == coord[0] and y == coord[1] + 1:
					self.maze_graph[(x, y)].append(coord)
				elif x == coord[0] and y == coord[1] - 1:
					self.maze_graph[(x, y)].append(coord)
				else:
					continue
		return(self.maze_graph)
	

	def findRoute(self,x1,y1,x2,y2):
		"""
		This method finds a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
		It returns the list of traversed coordinates followed along this route as a list of tuples (x,y),
		in the order in which the coordinates must be followed
		"""
		# this method calls the createMazeGraph method and conducts the depth-first search algorithm on the generated graph
		# to find a route from (x1, y1) to (x2, y2)
		# because the found route includes redundant paths, I take advantage of a peculiarity I noticed in the
		# sequences of stored coordinates in stack, explored and route, to remove redundant coordinates from the route
		start = (x1, y1)
		end = (x2, y2)
		explored = []
		maze_graph = self.createMazeGraph()
		stack = []                  
		route = []
		stack.append(start)                  
		explored.append(start)                
		while stack:                         
			current_pos = stack.pop()            
			route.append(current_pos)
			for neighbour in maze_graph[current_pos]:        
				if neighbour not in explored:       
					explored.append(neighbour)       
					stack.append(neighbour)      
					if neighbour == end:           
						route.append(neighbour)
						"""
						The code from here onwards takes advantage of a peculiarity I noticed
						in the sequences of coordinates in the lists of explored, stack and route.
						After removing remaining stack coordinates from the explored list, the non-redundant
						route coordinates in the explored and route lists will line up together, while the
						redundant coordinates will mismatch. For example:
						reduced_explored_list = [(7,8),{6,8},{8,8},(5,8),(4,8)]
						                route = [(7,8),{8,8},{6,8},(5,8),(4,8)]
						Where {} represents the mismatched values. 
						The "last index" for each subset of mismatched coordinates in "route" will capture the correct path coordinate
						What the following code does is to acquire that "last index" and filter the "route" list into "fast_route"
						"fast_route" will be the route without redundant steps taken by the search algorithm
						Note however, that "fast_route" does not always represent the shortest route
						"""
						reduced_explored_list = [coord for coord in explored if coord not in stack]
						position = []
						for i in range(len(reduced_explored_list)):
							if reduced_explored_list[i] == route[i]:
								position.append(i)
							else:
								continue
						correct_position = []
						for i in range(len(position)-1):
							if position[i+1] != position[i] + 1:
								correct_position.append(position[i+1]-1)
							else:
								continue
						fast_route_index = sorted(position+correct_position)
						fast_route = []
						for index in fast_route_index:
							fast_route.append(route[index])
						fast_route.append(route[-1])
						print(fast_route)
						return(fast_route)
		print([])
		return([])


def mazeTest():
	myMaze = Maze()
	myMaze.addCoordinate(1,0,0)
	myMaze.addCoordinate(1,1,0)
	myMaze.addCoordinate(7,1,0)
	myMaze.addCoordinate(1,2,0)
	myMaze.addCoordinate(2,2,0)
	myMaze.addCoordinate(3,2,0)
	myMaze.addCoordinate(4,2,0)
	myMaze.addCoordinate(6,2,0)
	myMaze.addCoordinate(7,2,0)
	myMaze.addCoordinate(4,3,0)
	myMaze.addCoordinate(7,3,0)
	myMaze.addCoordinate(4,4,0)
	myMaze.addCoordinate(7,4,0)
	myMaze.addCoordinate(3,5,0)
	myMaze.addCoordinate(4,5,0)
	myMaze.addCoordinate(7,5,0)
	myMaze.addCoordinate(1,6,0)
	myMaze.addCoordinate(2,6,0)
	myMaze.addCoordinate(3,6,0)
	myMaze.addCoordinate(4,6,0)
	myMaze.addCoordinate(5,6,0)
	myMaze.addCoordinate(6,6,0)
	myMaze.addCoordinate(7,6,0)
	myMaze.addCoordinate(5,7,0)
	myMaze.printMaze()
	#myMaze.createMazeGraph()
	#print(len(myMaze.maze_grid))
	myMaze.findRoute(1,1,5,7)
	myMaze.findRoute(7,1,1,0)
	myMaze.findRoute(1,1,7,7)
	#print(myMaze.maze_coords)
	#print(myMaze.special_coords)
	#print(myMaze.maze_open_areas)
	m = Maze()
	m.addCoordinate(0,0,1)
	m.addCoordinate(1,1,0)
	m.addCoordinate(1,3,0)
	m.addCoordinate(1,4,0)
	m.addCoordinate(1,5,0)
	m.addCoordinate(1,8,0)
	m.addCoordinate(2,1,0)
	m.addCoordinate(2,5,0)
	m.addCoordinate(2,8,0)
	m.addCoordinate(3,1,0)
	m.addCoordinate(3,2,0)
	m.addCoordinate(3,3,0)
	m.addCoordinate(3,4,0)
	m.addCoordinate(3,5,0)
	m.addCoordinate(3,8,0)
	m.addCoordinate(4,1,0)
	m.addCoordinate(4,5,0)
	m.addCoordinate(4,6,0)
	m.addCoordinate(4,7,0)
	m.addCoordinate(4,8,0)
	m.addCoordinate(5,1,0)
	m.addCoordinate(5,8,0)
	m.addCoordinate(6,1,0)
	m.addCoordinate(6,2,0)
	m.addCoordinate(6,3,0)
	m.addCoordinate(6,4,0)
	m.addCoordinate(6,8,0)
	m.addCoordinate(7,4,0)
	m.addCoordinate(7,5,0)
	m.addCoordinate(7,6,0)
	m.addCoordinate(7,7,0)
	m.addCoordinate(7,8,0)
	m.addCoordinate(8,8,0)
	m.addCoordinate(9,9,1)
	m.printMaze()
	m.findRoute(6,4,1,3)
	m.findRoute(4,6,6,4)
	m.findRoute(1,8,6,1)

def main():
	mazeTest()
	

if(__name__ == "__main__"):
	main()
