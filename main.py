import pygame
import sys
from puzzle import Puzzle

if __name__ == '__main__':
		w = 600
		h = 400

		pygame.init()

		#need a loop in case the user hits the back button

		outer_loop = 1

		while outer_loop:
			screen = pygame.display.set_mode((w, h))
			screen.fill((255, 255, 255))

			running = 1
			rect1 = pygame.Rect(0, 0, 600, 200)
			rect2 = pygame.Rect(0, 200, 600, 200)

			font = pygame.font.Font(None, 30)

			pygame.display.set_icon(pygame.image.load('objects/tile.bmp'))

			while running:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = 0
						outer_loop = 0

					if event.type == pygame.MOUSEBUTTONUP:
						pos = pygame.mouse.get_pos()
						if rect1.collidepoint(pos):
							puzzle = Puzzle(screen)
							outer_loop = puzzle.play()
							running = 0
							break
						elif rect2.collidepoint(pos):
							puzzle = Puzzle(screen)
							outer_loop = puzzle.user_create_puzzle()
							running = 0
							break

				#draw rectangles
				pygame.draw.rect(screen, (0, 0, 0), rect1, 1)
				pygame.draw.rect(screen, (0, 0, 0), rect2, 1)
				
				#render text
				text1 = font.render("Solve a puzzle", True, (0, 0, 0))
				text2 = font.render("Create your own puzzle", True, (0, 0, 0))
				screen.blit(text1, (w/2-75, h/4))
				screen.blit(text2, (w/2-125, 3*h/4))

				pygame.display.flip()
