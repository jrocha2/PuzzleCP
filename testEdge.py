from objects import *
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

edge = MiddleEdge(100, 100, GREEN, BLUE,10,100)
pygame.init()

screen = pygame.display.set_mode((500,500))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((255,255,255))
	edge.draw(screen)
	pygame.display.flip()

