import pygame
from boardEdge import *

class MiddleEdge:

	def __init__(self,xStart,yStart,topColor,bottomColor,shortEdge,longEdge):
		self.shortEdge = shortEdge
		self.longEdge = longEdge
		self.xStart = xStart
		self.yStart = yStart
		self.topBoardEdge = BoardEdge(xStart,yStart-self.shortEdge+1,0,topColor,shortEdge,longEdge)
		self.bottomBoardEdge = BoardEdge(xStart,yStart+self.longEdge,0,bottomColor,shortEdge,longEdge)

	def draw(self,screen):
		pygame.draw.rect(screen,(0,0,0),(self.xStart,self.yStart,self.longEdge,self.longEdge),1)
		self.topBoardEdge.draw(screen)
		self.bottomBoardEdge.draw(screen)

	def get_color(self):
		color1 = self.topBoardEdge.get_color()
		color2 = self.middleBoardEdge.get_color()
		return [color1, color2]

