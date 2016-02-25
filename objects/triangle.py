import pygame
from objects import *

class Triangle:

	def __init__(self, c, x_coord, y_coord, p):
		self.color = c #color -- this is a Color enum
		self.x = x_coord #x coordinate of upper left corner of tile
		self.y = y_coord #y coordinate of upper left corner of tile
		self.pos = p #position in the tile -- 1, 2, 3, 4

	def draw(self, screen, length):
		if self.pos==1:
			pygame.draw.polygon(screen, self.color, [(self.x, self.y), (self.x+length, self.y), (self.x + length/2, self.y+length/2)])
		if self.pos==2:
			pygame.draw.polygon(screen, self.color, [(self.x+length, self.y), (self.x+length, self.y+length), (self.x + length/2, self.y+length/2)])
		if self.pos==3:
			pygame.draw.polygon(screen, self.color, [(self.x+length, self.y+length), (self.x, self.y+length), (self.x + length/2, self.y+length/2)])
		if self.pos==4:
			pygame.draw.polygon(screen, self.color, [(self.x, self.y), (self.x, self.y+length), (self.x + length/2, self.y+length/2)])

	def get_color(self):
		return self.color
