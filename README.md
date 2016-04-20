# PuzzleCP
CSE-30151 Theory of Computing

### Instructions to Build and Run
- Ensure that Python v.2.7.9 or greater is installed
- Install pygame
- Run python script: `python main_menu.py`

### Instructions for Use  
##### Solving a Puzzle  
- Click a tile in the bottom row and a corresponding space in the puzzle to place it
- Click a tile that is already placed in the puzzle to rotate it
- Press 'd' while hovering over a tile in the puzzle to remove it
- Press 'q' at any time to quit the game
- Press "Solve" to fill in the puzzle with a solution. A solution tree is printed in the terminal for reference.
- Press "Check Solution" to check if the tiles currently in the puzzle are a correct solution. The transitions for the PDA are printed in the terminal for reference.

##### Creating a Puzzle
To fill in a given game piece with a color, first place the mouse over the piece. Pressing a key on the
keyboard at this point will fill it with a color according to the following options:  
- 'r' = Red
- 'b' = Blue
- 'g' = Green
- 'y' = Yellow
Once the puzzle and the tiles have been filled in, press "Solve" to fill in the puzzle if there is a solution. A solution tree is printed in the terminal for reference. If there is no solution to the puzzle, this is printed to the screen.
