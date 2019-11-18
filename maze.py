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
		self.maze_grid = []
		pass

	def addCoordinate(self,x,y,blockType):
		"""
		Add information about a coordinate on the maze grid
		x is the x coordinate
		y is the y coordinate
		blockType: 0 for an open space and 1 for a wall
		"""
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
		Print out an ascii representation of the maze.
		A * indicates a wall and a empty space indicates an open space in the maze
		"""
		grid = []
		for i in range(self.height + 1):
			row = []
			i_columns = [tup for tup in self.special_coords if tup[1] == i]
			sorted_columns = sorted(i_columns, key=lambda tup: tup[0], reverse=True)
			for x in range(self.width + 1):
				if x not in [tup[0] for tup in sorted_columns]:
					row.append('*')
					self.maze_coords.append((x,i,1))
				elif sorted_columns.pop()[2] == 0: # if x is not one of the special coord's x then that x must be the referring to the first popped tuple in the reverse ordered list of special coords
					row.append(' ')
					self.maze_coords.append((x,i,0))
				else:
					row.append('*')
					self.maze_coords.append((x,i,1))
			print(row)
			grid.append(row)
		self.maze_grid = grid
		self.maze_walls = [(coord[0],coord[1]) for coord in self.maze_coords if coord[2]==1]
		self.maze_open_areas = [(coord[0],coord[1]) for coord in self.maze_coords if coord[2]==0]
		pass
	
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
		print(self.maze_graph)
		pass


	def findRoute(self,x1,y1,x2,y2):
		start = (x1, y1)
		end = (x2, y2)
		explored = []
		stack = []                  
		route = []
		stack.append(start)                  
		explored.append(start)                
		while stack:                         
			current_pos = stack.pop()            
			route.append(current_pos)
			for neighbour in self.maze_graph[current_pos]:        
				if neighbour not in explored:       
					explored.append(neighbour)       
					stack.append(neighbour)         
					if neighbour == end:           
						route.append(neighbour)
						print(route)
						return(route)
		print([])
		return([])

		# create graph based on coords not in self.maze_walls using dictionary
		#for coord in self.maze_coords not in self.maze_walls:
		# conduct depth first search on graph
		
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
	myMaze.createMazeGraph()
	#print(len(myMaze.maze_grid))
	myMaze.findRoute(1,1,5,7)
	myMaze.findRoute(7,1,1,0)
	myMaze.findRoute(1,1,7,7)
	#print(myMaze.maze_coords)
	#print(myMaze.special_coords)
	#print(myMaze.maze_open_areas)

def main():
	mazeTest()

if(__name__ == "__main__"):
	main()
