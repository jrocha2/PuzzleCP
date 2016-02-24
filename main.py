import pygame
#from objects import *
from objects.tile import Tile
from objects.triangle import *

if __name__ == '__main__':

	test = Tile(5, 5, Color.blue, Color.yellow, Color.green, Color.red)



	pygame.init()
	screen = pygame.display.set_mode((640,400))

	running = 1

	while running:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running =0
		screen.fill((0,0,0))
		pygame.display.flip()
