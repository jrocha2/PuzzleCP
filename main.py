import pygame
from objects.tile import Tile
from objects.triangle import *

if __name__ == '__main__':

	test = Tile(5, 5, 100, blue, yellow, green, red)



	pygame.init()
	screen = pygame.display.set_mode((640,400))

	running = 1

	while running:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running =0
		screen.fill((0,0,0))
		test.draw(screen)
		pygame.display.flip()
