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

		#self.tileList is list of possible tiles, self.solutionList is list of actual tiles that solve puzzle
		#puzzleList is list of tiles that user has added to solve the puzzle
		self.tileList = []
		self.solutionList = []
		self.puzzleList = []

		#height and width
		self.h = 400
		self.w = 600
		self.tile_size = 75

	def create_random_puzzle(self):
		
		#x and y coordinates of upper left of first tile
		space = 50
		x = get_print_start_point(self.w,space,self.numberOfTiles,self.tile_size)
		y = 250
		s = self.tile_size + space#space b/t tiles
		blankTile = Tile(600,600,self.tile_size,(WHITE,WHITE,WHITE,WHITE))

		#make tiles based on previous tile color
		self.tileList.append(Tile(x, y, self.tile_size))
		self.solutionList.append(blankTile)
		for i in range(1,self.numberOfTiles):
			self.tileList.append(Tile(x+i*s, y,self.tile_size,self.tileList[i-1].get_right_color()))
			self.solutionList.append(blankTile)

		#puzzle draw
		xP = get_print_start_point(self.w,0,self.puzzleSize,self.tile_size)
		yP = 75
		sP = 75 #space between pieces
		shortEdge = 12.5

		#generate puzzle based on tile colors
		self.puzzleList.append(get_front_of_puzzle(self.tileList[0],xP,yP,self.tile_size,shortEdge))
		for k in range(1,self.puzzleSize-1):
			self.puzzleList.append(get_middle_of_puzzle(self.tileList[k],xP+k*sP,yP,self.tile_size,shortEdge))
		self.puzzleList.append(get_end_of_puzzle(self.tileList[self.puzzleSize-1],xP+(self.puzzleSize-1)*sP,yP,self.tile_size,shortEdge))

		#random shuffle of self.tileList
		self.tileList = shuffle_tile(self.tileList,self.numberOfTiles)

	def play(self):

		self.numberOfTiles = random.randint(4,10)
		self.puzzleSize = self.numberOfTiles

		self.w = get_window_width(self.puzzleSize,self.numberOfTiles)

		#set up puzzle and tiles for user's selection
		self.create_random_puzzle()

		#current selected tile
		currentTile = 0
		
		blankTile = Tile(600,600,self.tile_size,(WHITE,WHITE,WHITE,WHITE))

		#pygame.init()
		screen = pygame.display.set_mode((self.w, self.h))
		pygame.display.set_caption("Course Project 1: Interactive Puzzle")
		pygame.display.set_icon(pygame.image.load('objects/tile.bmp'))

		running = 1
		solved = False

		while running:

			#check events
			event = pygame.event.poll()
			if event.type == pygame.QUIT:
				running =0
				#pygame.display.quit()
				#pygame.quit()
				#break

			#print to screen
			screen.fill(WHITE)
			for piece in self.puzzleList:
				piece.draw(screen)
			for tile in self.tileList:
				tile.draw(screen)
			for solution in self.solutionList:
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
					for piece in self.puzzleList:
						currentPiece += 1
						if piece.is_inside(pos):
							self.solutionList[currentPiece-1] = blankTile

			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()

				#get number of tile from self.tileList (lower tiles) if one was clicked
				#currentTile is number of selected tile from choices
				place = 0
				for tile in self.tileList:
					place += 1
					if tile.is_inside(pos):
						if currentTile == 0:
							currentTile += place

				#iterate through each piece in puzzleList (upper tiles)
				#check to see if mouse click was inside each piece
				currentPiece = 0
				for piece in self.puzzleList:
					currentPiece += 1
					if piece.is_inside(pos):
						#if user has selected a tile to place
						if currentTile != 0:
							print currentTile
							rect = piece.get_rect() #rect for piece in puzzleList
							tile = Tile(rect[0],rect[1],rect[2],self.tileList[currentTile-1].get_color()) #create tile to place in puzzle
							self.solutionList[currentPiece-1] = tile #place in puzzle

#						#if user has not selected a tile to place
#						else:
#							#if selected tile in puzzle is not blank
#							if self.solutionList[currentPiece-1] != blankTile:
#								rect = piece.get_rect() #rect for piece in puzzleList
#								c = self.solutionList[currentPiece-1].get_color() #get color list for tiles
#								newColors = ((c[3], c[0], c[1], c[2]))
#								tile = Tile(rect[0], rect[1], rect[2], newColors) #create new tile to replace the old one
#								self.solutionList[currentPiece-1] = tile #place in puzzle

						currentTile = 0
							
					# Display solution status
					font = pygame.font.Font(None, 30)
					text = ''
					if solved:
						text = font.render("Valid Solution", True, GREEN)
					else: 
						text = font.render("Valid Solution", True, WHITE)
					screen.blit(text, (self.w/2-75, self.h/2))

			pygame.display.flip()