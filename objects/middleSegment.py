import pygame
from boardEdge import *

class MiddleEdge:

	def __init__(self,xStart,yStart,topColor,bottomColor,shortEdge,longEdge):
		self.shortEdge = shortEdge
		self.longEdge = longEdge
		self.xStart = xStart
		self.yStart = yStart
		self.middleEdge = pygame.Rect(self.xStart,self.yStart,self.longEdge,self.longEdge)
		self.topBoardEdge = BoardEdge(xStart,yStart-self.shortEdge+1,0,topColor,shortEdge,longEdge)
		self.bottomBoardEdge = BoardEdge(xStart,yStart+self.longEdge,0,bottomColor,shortEdge,longEdge)
		self.edges = [self.topBoardEdge, self.bottomBoardEdge]

	def draw(self,screen):
		pygame.draw.rect(screen,(0,0,0),(self.xStart,self.yStart,self.longEdge,self.longEdge),1)
		self.topBoardEdge.draw(screen)
		self.bottomBoardEdge.draw(screen)

	def get_color(self):
		color1 = self.topBoardEdge.get_color()
		color2 = self.bottomBoardEdge.get_color()
		return [color1, color2]

	def is_inside(self,pos):
		return self.middleEdge.collidepoint(pos)

	def get_rect(self):
		return self.middleEdge
	
	def is_inside_top(self, pos):
		return self.topBoardEdge.is_inside(pos)

	def is_inside_bottom(self, pos):
		return self.bottomBoardEdge.is_inside(pos)

	def set_bottom_color(self, color):
		self.bottomBoardEdge.set_color(color)

	def set_top_color(self, color):
		self.topBoardEdge.set_color(color)

	def is_colored(self):
		for edge in self.edges:
			if edge.get_color() == (255, 255, 255):
				return 0
		return 1
