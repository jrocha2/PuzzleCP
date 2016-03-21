from triangle import *
import pygame
from pygame import rect
import random
from numpy.random import choice
class Tile:

	#option to pass in the colors yourself
	def __init__(self, x_coord, y_coord, length, colors = None):
		self.x = x_coord #x coordinate of upper left corner
		self.y = y_coord #y coordinate of upper left corner
		self.length = length
		self.tile = pygame.Rect(self.x-1,self.y-1,self.length+3,self.length+3)
		self.colors = colors

		if colors == None:
			self.colors = self.generate_colors()

		elif colors == "blank":
			self.colors = ((255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255))
		elif len(colors) != 4:
			left_color = colors
			self.colors = self.generate_colors()
			lst = list(self.colors)
			lst[3] = left_color
			self.colors = tuple(lst)

		#create tiles with specified colors
		self.t1 = Triangle(self.colors[0], x_coord, y_coord, 1, 75)
		self.t2 = Triangle(self.colors[1], x_coord, y_coord, 2, 75)
		self.t3 = Triangle(self.colors[2], x_coord, y_coord, 3, 75)
		self.t4 = Triangle(self.colors[3], x_coord, y_coord, 4, 75)

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

	#set color of tiles; colors input is a tuple
	def set_color(self, colors):
		self.colors = colors
		self.t1.set_color(colors[0])
		self.t2.set_color(colors[1])
		self.t3.set_color(colors[2])
		self.t4.set_color(colors[3])

	def is_inside(self,pos):
		return self.tile.collidepoint(pos)

	def get_right_color(self):
		return self.colors[1]

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

	#rotates colors of triangles in tile
	def rotate_tile(self):
		weights = [.4, .3, .2, .1]
		nRotate = choice(xrange(4), p=weights) #get number to rotate by
		colors_temp = self.get_color() #store colors temporarily here

		#rotate colors
		self.t1.set_color(colors_temp[(0+nRotate)%4])
		self.t2.set_color(colors_temp[(1+nRotate)%4])
		self.t3.set_color(colors_temp[(2+nRotate)%4])
		self.t4.set_color(colors_temp[(3+nRotate)%4])

	#returns -1 if not inside tile; otherwise returns number of triangle that pos is in
	def is_inside_triangle(self, pos):
		if not self.is_inside(pos):
			return -1

		elif self.t1.is_inside(pos):
			return 1
		elif self.t2.is_inside(pos):
			return 2
		elif self.t3.is_inside(pos):
			return 3
		elif self.t4.is_inside(pos):
			return 4
