import pygame
from objects import *

def checkSolution(pL, tL):
    # Number of tiles in puzzle
    n = 4

    # Check Front Tile against Puzzle
    tileColors = tL[n].get_color()
    tileColors.pop(1)   # remove irrelevant color
    if pL[0].get_color() != tileColors :
        return False 

    # Check Back Tile against Puzzle
    tileColors = tL[2*n-1].get_color()
    tileColors.pop(3)   # remove irrelevant color
    if pL[n-1].get_color() != tileColors :
        return False

    # Check Middle Tiles against Puzzle
    for l in range(1, n-1):
        tileColors = tL[l+n].get_color()
        tileColors.pop(3)       # remove irrelevant colors
        tileColors.pop(1)
        if pL[l].get_color() != tileColors :
            return False

    # Check Tiles against each other
    for l in range(n, 2*n-2) :
        if tL[l].get_color()[1] != tL[l+1].get_color()[3] :
            return False
    
    return True

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
	solutionList = []
	blankTile = Tile(600,600,tile_size,(WHITE,WHITE,WHITE,WHITE))

	tileList.append(Tile(x, y, tile_size, colorList[0]))
	tileList.append(Tile(x+s, y, tile_size, colorList[1]))
	tileList.append(Tile(x+2*s, y, tile_size, colorList[2]))
	tileList.append(Tile(x+3*s, y, tile_size, colorList[3]))
	solutionList.append(blankTile)
	solutionList.append(blankTile)
	solutionList.append(blankTile)
	solutionList.append(blankTile)

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
	pygame.display.set_caption("Course Project 1: Interactive Puzzle")
	pygame.display.set_icon(pygame.image.load('objects/tile.bmp'))

	running = 1
        solved = False

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
					currentTile += place

			#iterate through each piece in puzzleList (upper tiles)
			#check to see if mouse click was inside each piece
			currentPiece = 0
			for piece in puzzleList:
				currentPiece += 1
				if piece.is_inside(pos):
					print currentPiece
					#if user has selected a tile to place
					if currentTile != 0:
						rect = piece.get_rect() #rect for piece in puzzleList
						tile = Tile(rect[0],rect[1],rect[2],colorList[currentTile%4-1]) #create tile to place in puzzle
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

