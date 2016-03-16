from triangle import *
import pygame
from pygame import rect
import random

class Tile:

	#option to pass in the colors yourself
	def __init__(self, x_coord, y_coord, length, colors = None):
		self.x = x_coord #x coordinate of upper left corner
		self.y = y_coord #y coordinate of upper left corner
		self.length = length
		self.tile = pygame.Rect(self.x-1,self.y-1,self.length+3,self.length+3)

		if colors == None:
			colors = self.generate_colors()

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

                #draw tile dividing lines
                pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + self.length, self.y + self.length))
                pygame.draw.line(screen, BLACK, (self.x, self.y + self.length), (self.x + self.length, self.y))

	#returns list of colors in order: 1, 2, 3, 4
	def get_color(self):
		return (self.t1.get_color(), self.t2.get_color(), self.t3.get_color(), self.t4.get_color())


	def is_inside(self,pos):
		return self.tile.collidepoint(pos)

	#returns tuple of four colors
	def generate_colors(self):
		random.seed(None) #seed

		a = ()

		#generate four random numbers and use to choose colors
		for i in range(4):
			r = random.randint(1,4) #generate a number 1 through 4

			if r==1:
				a += (GREEN,)

			elif r==2:
				a += (YELLOW,)
			
			elif r==3:
				a += (BLUE,)

			elif r==4:
				a += (RED,)

		return a

