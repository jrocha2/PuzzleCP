import pygame
from boardEdge import *

class BackEdge:

	def __init__(self,xStart,yStart,topColor,middleColor,bottomColor,shortEdge,longEdge):
		self.shortEdge = shortEdge
		self.longEdge = longEdge
		self.xStart = xStart
		self.yStart = yStart
		self.backEdge = pygame.Rect(self.xStart,self.yStart,self.longEdge,self.longEdge)
		self.topBoardEdge = BoardEdge(xStart,yStart-self.shortEdge+1,0,topColor,shortEdge,longEdge)
		self.middleBoardEdge = BoardEdge(xStart+self.longEdge,yStart,1,middleColor,shortEdge,longEdge)
		self.bottomBoardEdge = BoardEdge(xStart,yStart+self.longEdge,0,bottomColor,shortEdge,longEdge)

	def draw(self,screen):
		pygame.draw.rect(screen,(0,0,0),self.backEdge,1)
		self.topBoardEdge.draw(screen)
		self.middleBoardEdge.draw(screen)
		self.bottomBoardEdge.draw(screen)

	def get_color(self):
		color1 = self.topBoardEdge.get_color()
		color2 = self.middleBoardEdge.get_color()
		color3 = self.bottomBoardEdge.get_color()
		return [color1, color2, color3]

	def is_inside(self,pos):
		return self.backEdge.collidepoint(pos)

	def get_rect(self):
		return self.backEdge

	def is_inside_top(self, pos):
		return self.topBoardEdge.is_inside(pos)

	def is_inside_bottom(self, pos):
		return self.bottomBoardEdge.is_inside(pos)

	def is_inside_middle(self, pos):
		return self.middleBoardEdge.is_inside(pos)
