from triangle import Triangle
import pygame
from pygame import rect

class Tile:
	def __init__(self, x_coord, y_coord, length, colors):
		self.x = x_coord #x coordinate of upper left corner
		self.y = y_coord #y coordinate of upper left corner
		self.length = length
		self.tile = pygame.Rect(self.x-1,self.y-1,self.length+3,self.length+3)

		#create tiles with specified colors
		self.t1 = Triangle(colors[0], x_coord, y_coord, 1)
		self.t2 = Triangle(colors[1], x_coord, y_coord, 2)
		self.t3 = Triangle(colors[2], x_coord, y_coord, 3)
		self.t4 = Triangle(colors[3], x_coord, y_coord, 4)

	def draw(self, screen):
		#draw black square
		pygame.draw.rect(screen, (0,0,0), self.tile)

		#draw triangles
		self.t1.draw(screen, self.length)
		self.t2.draw(screen, self.length)
		self.t3.draw(screen, self.length)
		self.t4.draw(screen, self.length)

	#returns list of colors in order: 1, 2, 3, 4
	def get_color(self):
		return [self.t1.get_color(), self.t2.get_color(), self.t3.get_color(), self.t4.get_color()]


	def is_inside(self,pos):
		return self.tile.collidepoint(pos)
