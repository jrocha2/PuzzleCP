#colored edge of puzzle
import pygame
class BoardEdge:
	shortEdge = 10
	longEdge = 100

	def __init__(self,xStart,yStart,orientation,color):
		self.xStart = xStart
		self.yStart = yStart
		self.orientation = orientation
		self.color = color

	def draw(self,screen):
		if self.orientation == 1:
			pygame.draw.rect(screen,self.color,(self.xStart,self.yStart,self.shortEdge,self.longEdge))
		else:
			pygame.draw.rect(screen,self.color,(self.xStart,self.yStart,self.longEdge,self.shortEdge))

	def get_color(self):
		return self.color

		
