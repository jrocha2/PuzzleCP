from enum import Enum

Color = Enum('Color', 'red yellow green blue')

class Triangle:

	def __init__(self, c, x_coord, y_coord, p):
		self.color = c #color -- this is a Color enum
		self.x = x_coord #x coordinate of upper left corner of tile
		self.y = y_coord #y coordinate of upper left corner of tile
		self.pos = p #position in the tile -- 1, 2, 3, 4

