import pygame
from objects import *
import random

def get_window_width(puzzleSize,numberOfTiles):
	tileLength = 150 + 125*numberOfTiles
	puzzleLength = 200+75*puzzleSize

	if tileLength > puzzleLength:
		return tileLength
	else:
		return puzzleLength

def get_print_start_point(windowWidth, spaceBetweenTile, numberOfTile, tileSize):
	puzzleWidth = numberOfTile*tileSize + (numberOfTile-1)*spaceBetweenTile
	start = (windowWidth-puzzleWidth)/2
	return start

def get_front_of_puzzle(tile,x,y,tile_size,short_edge):
	color = tile.get_color()
	puzzle = FrontEdge(x,y,color[0],color[3],color[2],short_edge,tile_size) 
	return puzzle

def get_middle_of_puzzle(tile,x,y,tile_size,short_edge):
	color = tile.get_color()
	puzzle = MiddleEdge(x,y,color[0],color[2],short_edge,tile_size) 
	return puzzle

def get_end_of_puzzle(tile,x,y,tile_size,short_edge):
	color = tile.get_color()
	puzzle = BackEdge(x,y,color[0],color[1],color[2],short_edge,tile_size) 
	return puzzle

def shuffle_tile(tileList,numberOfTiles):

	#for each tile, swap with another random tile
	for x in xrange(numberOfTiles):
		colors_temp = tileList[x].get_color()
		n = random.randint(0, numberOfTiles-1) #random tile number to swap with
		tileList[x].set_color(tileList[n].get_color())
		tileList[n].set_color(colors_temp)

	tileList = rotate_tile(tileList, numberOfTiles)

	return tileList #return randomly swapped and rotated tiles

def rotate_tile(tileList, numberOfTiles):

	for x in xrange(numberOfTiles):
			tileList[x].rotate_tile()
	return tileList
		

class puzzle:

	def __init__(self):
		x = 5

	def play(self):

		numberOfTiles = random.randint(4,10)
		puzzleSize = numberOfTiles

		#height and width
		h = 400
		w = get_window_width(puzzleSize,numberOfTiles)

		tile_size = 75

		#x and y coordinates of upper left of first tile
		space = 50
		x = get_print_start_point(w,space,numberOfTiles,tile_size)
		y = 250
		s = tile_size + space#space b/t tiles
		tileList = []
		solutionList = []
		blankTile = Tile(600,600,tile_size,(WHITE,WHITE,WHITE,WHITE))

		"""tileList.append(Tile(x, y, tile_size, colorList[0]))
		tileList.append(Tile(x+s, y, tile_size, colorList[1]))
		tileList.append(Tile(x+2*s, y, tile_size, colorList[2]))
		tileList.append(Tile(x+3*s, y, tile_size, colorList[3]))
		solutionList.append(blankTile)
		solutionList.append(blankTile)
		solutionList.append(blankTile)
		solutionList.append(blankTile)"""

		#make tiles based on previous tile color
		tileList.append(Tile(x, y, tile_size))
		solutionList.append(blankTile)
		for i in range(1,numberOfTiles):
			tileList.append(Tile(x+i*s, y,tile_size,tileList[i-1].get_right_color()))
			solutionList.append(blankTile)

		#puzzle draw
		xP = get_print_start_point(w,0,puzzleSize,tile_size)
		yP = 75
		sP = 75 #space between pieces
		shortEdge = 12.5
		puzzleList = []

		#generate puzzle based on tile colors
		puzzleList.append(get_front_of_puzzle(tileList[0],xP,yP,tile_size,shortEdge))
		for k in range(1,puzzleSize-1):
			puzzleList.append(get_middle_of_puzzle(tileList[k],xP+k*sP,yP,tile_size,shortEdge))
		puzzleList.append(get_end_of_puzzle(tileList[puzzleSize-1],xP+(puzzleSize-1)*sP,yP,tile_size,shortEdge))


		#random shuffle of tileList
		tileList = shuffle_tile(tileList,numberOfTiles)

		#current selected tile
		currentTile = 0

		#pygame.init()
		screen = pygame.display.set_mode((w, h))
		pygame.display.set_caption("Course Project 1: Interactive Puzzle")
		pygame.display.set_icon(pygame.image.load('objects/tile.bmp'))

		running = 1
		solved = False

		while running:

			#check events
			event = pygame.event.poll()
			if event.type == pygame.QUIT:
				running =0
				pygame.display.quit()
				pygame.quit()
				break

			#print to screen
			screen.fill(WHITE)
			for piece in puzzleList:
				piece.draw(screen)
			for tile in tileList:
				tile.draw(screen)
			for solution in solutionList:
				solution.draw(screen)

			#check if user has pressed a key
			if event.type == pygame.KEYUP:

				#quit
				if event.key == pygame.K_q:
					running = 0
			
				#delete
				if event.key == pygame.K_d:
					pos = pygame.mouse.get_pos()

					#iterate through pieces in puzzleList to see if mouse is inside
					currentPiece = 0
					for piece in puzzleList:
						currentPiece += 1
						if piece.is_inside(pos):
							solutionList[currentPiece-1] = blankTile

			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()

				#get number of tile from tileList (lower tiles) if one was clicked
				#currentTile is number of selected tile from choices
				place = 0
				for tile in tileList:
					place += 1
					if tile.is_inside(pos):
						if currentTile == 0:
							currentTile += place

				#iterate through each piece in puzzleList (upper tiles)
				#check to see if mouse click was inside each piece
				currentPiece = 0
				for piece in puzzleList:
					currentPiece += 1
					if piece.is_inside(pos):
						#if user has selected a tile to place
						if currentTile != 0:
							rect = piece.get_rect() #rect for piece in puzzleList
							tile = Tile(rect[0],rect[1],rect[2],tileList[currentTile-1].get_color()) #create tile to place in puzzle
							solutionList[currentPiece-1] = tile #place in puzzle

						#if user has not selected a tile to place
						else:
							#if selected tile in puzzle is not blank
							if solutionList[currentPiece-1] != blankTile:
								rect = piece.get_rect() #rect for piece in puzzleList
								c = solutionList[currentPiece-1].get_color() #get color list for tiles
								newColors = ((c[3], c[0], c[1], c[2]))
								tile = Tile(rect[0], rect[1], rect[2], newColors) #create new tile to replace the old one
								solutionList[currentPiece-1] = tile #place in puzzle

						currentTile = 0
							
					"""# If puzzle is filled, check solution
					for i in range(4,8):
						if tileList[i] == blankTile:
							solved = False
							break
						elif i == 7:
							solved = checkSolution(puzzleList, tileList)
					"""

					# Display solution status
					font = pygame.font.Font(None, 30)
					text = ''
					if solved:
						text = font.render("Valid Solution", True, GREEN)
					else: 
						text = font.render("Valid Solution", True, WHITE)
					screen.blit(text, (w/2-75, h/2))

			pygame.display.flip()
		#pygame.display.quit()
