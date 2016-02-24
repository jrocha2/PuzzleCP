from triangle import Triangle

class Tile:
	def __init__(self, x_coord, y_coord, c1, c2, c3, c4):
		self.x = x_coord #x coordinate of upper left corner
		self.y = y_coord #y coordinate of upper left corner

		#create tiles with specified colors
		self.t1 = Triangle(c1, x_coord, y_coord, 1)
		self.t2 = Triangle(c2, x_coord, y_coord, 2)
		self.t3 = Triangle(c3, x_coord, y_coord, 3)
		self.t4 = Triangle(c4, x_coord, y_coord, 4)

