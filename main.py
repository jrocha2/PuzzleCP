import pygame
from objects import *

if __name__ == '__main__':

	#height and width
	h = 400
	w = 640

	tile_size = 75

	#x and y coordinates of upper left of first tile
	x = 100
	y = 250
	s = 125 #space b/t tiles

	t1 = Tile(x, y, tile_size, GREEN, BLUE, BLUE, BLUE)
	t2 = Tile(x+s, y, tile_size, GREEN, YELLOW, BLUE, BLUE)
	t3 = Tile(x+2*s, y, tile_size, BLUE, RED, GREEN, YELLOW)
	t4 = Tile(x+3*s, y, tile_size, BLUE, RED, GREEN, RED)

	#puzzle draw
	xP = 175
	yP = 75
	sP = 75 #space between pieces

	p1 = FrontEdge(xP,yP,GREEN,BLUE,BLUE,12.5,tile_size)
	p2 = MiddleEdge(xP+sP,yP,GREEN,BLUE,12.5,tile_size)
	p3 = MiddleEdge(xP+2*sP,yP,BLUE,GREEN,12.5,tile_size)
	p4 = BackEdge(xP+3*sP,yP,BLUE,RED,GREEN,12.5,tile_size)

	pygame.init()
	screen = pygame.display.set_mode((w, h))

	running = 1

	while running:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running =0
		screen.fill(WHITE)
		p1.draw(screen)
		p2.draw(screen)
		p3.draw(screen)
		p4.draw(screen)
		t1.draw(screen)
		t2.draw(screen)
		t3.draw(screen)
		t4.draw(screen)
		pygame.display.flip()
