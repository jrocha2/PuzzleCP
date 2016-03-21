import pygame

#define colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#pass in a position and list of points to determine if the point lies within the polygon
def point_in_poly(pos, poly):

	x = pos[0]
	y = pos[1]

	n = len(poly)
	inside = False

	p1x,p1y = poly[0]
	for i in range(n+1):
		p2x,p2y = poly[i % n]
		if y > min(p1y,p2y):
			if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xints:
						inside = not inside
		p1x,p1y = p2x,p2y

	return inside
class Triangle:

	def __init__(self, c, x_coord, y_coord, p, length):
		self.color = c #color -- this is a Color enum
		self.x = x_coord #x coordinate of upper left corner of tile
		self.y = y_coord #y coordinate of upper left corner of tile
		self.pos = p #position in the tile -- 1, 2, 3, 4

		if self.pos==1:
			 self.points = [(self.x, self.y), (self.x+length, self.y), (self.x + length/2, self.y+length/2)]
		if self.pos==2:
			self.points = [(self.x+length, self.y), (self.x+length, self.y+length), (self.x + length/2, self.y+length/2)]
		if self.pos==3:
			self.points = [(self.x+length, self.y+length), (self.x, self.y+length), (self.x + length/2, self.y+length/2)]
		if self.pos==4:
			self.points = [(self.x, self.y), (self.x, self.y+length), (self.x + length/2, self.y+length/2)]

	def draw(self, screen, length):
			pygame.draw.polygon(screen, self.color, self.points) 

	def get_color(self):
		return self.color

	#set color of triangle
	def set_color(self, color):
		self.color = color
	
	def is_inside(self, pos):
		return point_in_poly(pos, self.points)
