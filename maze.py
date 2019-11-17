import itertools

class Maze:
	def __init__(self):
		self.height = 0
		self.width = 0
		self.special_coords = []
		pass

	def addCoordinate(self,x,y,blockType):
		"""
		Adds information about a coordinate on the maze grid
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
		Prints out an ascii representation of the maze.
		A * indicates a wall and a empty space indicates an open space in the maze
		"""
		for i in range(self.height + 1):
			row = ''
			i_columns = [tup for tup in self.special_coords if tup[1] == i]
			sorted_columns = sorted(i_columns, key=lambda tup: tup[0], reverse=True)
			for x in range(self.width + 1):
				if x not in [tup[0] for tup in sorted_columns]:
					row += '*'
				elif sorted_columns.pop()[2] == 0: # if x is not one of the special coord's x then that x must be the referring to the first popped tuple in the reverse ordered list of special coords
					row += ' '
				else:
					row += '*'
			print(row)
		pass

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

def main():
	mazeTest()

if(__name__ == "__main__"):
	main()
