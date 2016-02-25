from triangle import Triangle
import pygame

class Tile:
	def __init__(self, x_coord, y_coord, length, c1, c2, c3, c4):
		self.x = x_coord #x coordinate of upper left corner
		self.y = y_coord #y coordinate of upper left corner
		self.length = length

		#create tiles with specified colors
		self.t1 = Triangle(c1, x_coord, y_coord, 1)
		self.t2 = Triangle(c2, x_coord, y_coord, 2)
		self.t3 = Triangle(c3, x_coord, y_coord, 3)
		self.t4 = Triangle(c4, x_coord, y_coord, 4)

	def draw(self, screen):
		#draw black square
		pygame.draw.rect(screen, (0,0,0), (self.x-1,self.y-1,self.length+3,self.length+3))

		#draw triangles
		self.t1.draw(screen, self.length)
		self.t2.draw(screen, self.length)
		self.t3.draw(screen, self.length)
		self.t4.draw(screen, self.length)

	#returns list of colors in order: 1, 2, 3, 4
	def get_colors(self):
		return [self.t1.get_color(), self.t2.get_color(), self.t3.get_color(), self.t4.get_color()]
