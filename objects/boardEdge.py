#colored edge of puzzle
import pygame
class BoardEdge:

	def __init__(self,xStart,yStart,orientation,color,shortEdge,longEdge):
		self.xStart = xStart
		self.yStart = yStart
		self.orientation = orientation
		self.color = color
		self.shortEdge = shortEdge
		self.longEdge = longEdge

	def draw(self,screen):
		if self.orientation == 1:
			pygame.draw.rect(screen,self.color,(self.xStart,self.yStart,self.shortEdge,self.longEdge))
		else:
			pygame.draw.rect(screen,self.color,(self.xStart,self.yStart,self.longEdge,self.shortEdge))

	def get_color(self):
		return self.color

		
