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
	colorList = []
	colorList.append((GREEN, BLUE, BLUE, BLUE))
	colorList.append((GREEN, YELLOW, BLUE, BLUE))
	colorList.append((BLUE, RED, GREEN, YELLOW))
	colorList.append((BLUE, RED, GREEN, RED))
	tileList = []
	blankTile = Tile(600,600,tile_size,(WHITE,WHITE,WHITE,WHITE))

	tileList.append(Tile(x, y, tile_size, colorList[0]))
	tileList.append(Tile(x+s, y, tile_size, colorList[1]))
	tileList.append(Tile(x+2*s, y, tile_size, colorList[2]))
	tileList.append(Tile(x+3*s, y, tile_size, colorList[3]))
	tileList.append(blankTile)
	tileList.append(blankTile)
	tileList.append(blankTile)
	tileList.append(blankTile)

	#puzzle draw
	xP = 175
	yP = 75
	sP = 75 #space between pieces
	shortEdge = 12.5
	puzzleList = []

	puzzleList.append(FrontEdge(xP,yP,GREEN,BLUE,BLUE,shortEdge,tile_size))
	puzzleList.append(MiddleEdge(xP+sP,yP,GREEN,BLUE,shortEdge,tile_size))
	puzzleList.append(MiddleEdge(xP+2*sP,yP,BLUE,GREEN,shortEdge,tile_size))
	puzzleList.append(BackEdge(xP+3*sP,yP,BLUE,RED,GREEN,shortEdge,tile_size))

	#current selected tile
	currentTile = 0

	pygame.init()
	screen = pygame.display.set_mode((w, h))

	running = 1

	while running:

		#check events
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running =0

		#print to screen
		screen.fill(WHITE)
		for piece in puzzleList:
			piece.draw(screen)
		for tile in tileList:
			tile.draw(screen)

		#check if user has pressed the mouse
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()

			#get number of tile from tileList (lower tiles) if one was clicked
			#currentTile is number of selected tile from choices
			for l in range(0,4):
				if tileList[l].is_inside(pos):
					currentTile = l+1

			#iterate through each piece in puzzleList (upper tiles)
			#check to see if mouse click was inside each piece
			currentPiece = 0
			for piece in puzzleList:
				currentPiece += 1
				if piece.is_inside(pos):
					#if user has selected a tile to place
					if currentTile != 0:
						rect = piece.get_rect() #rect for piece in puzzleList
						tile = Tile(rect[0],rect[1],rect[2],colorList[currentTile%4-1]) #create tile to place in puzzle
						tileList[currentPiece+3] = tile #place in puzzle

					#if user has not selected a tile to place
					else:
						#if selected tile in puzzle is not blank
						if tileList[currentPiece+3] != blankTile:
							rect = piece.get_rect() #rect for piece in puzzleList
							c = tileList[currentPiece+3].get_colors() #get color list for tiles
							newColors = ((c[3], c[0], c[1], c[2]))
							tile = Tile(rect[0], rect[1], rect[2], newColors) #create new tile to replace the old one
							tileList[currentPiece+3] = tile #place in puzzle

					currentTile = 0
		pygame.display.flip()
