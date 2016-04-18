from objects import *
from collections import deque
from sets import Set

    #################################################################################
### For the purpose of this file, "tile" refers simply to the colors of a given tile ###
    #################################################################################

class Node(object):
    # Node with no parent/tile data is the root
    def __init__(self):
        self.tile = None        # This state's color layout
        self.children = []      # List of children
        self.parent = None      # Parent Node
        self.depth = 0    # This node's depth in a tree where 0 is the root node

    # Add a tile to current node's children pointing to it as parent 
    def add_child(self, tile):
        node = Node()
        node.tile = tile
        node.parent = self
        node.depth = self.depth + 1
        self.children.append(node)

    def get_right_color(self):
        return self.tile[1]

    # Helper functions to make printing of nodes and trees nicer
    def __str__(self, level=0):
        string = "    "*level+ str(level) + "-->" + self.get_color_string(self.tile) + "\n"
        for child in self.children:
            string += child.__str__(level+1)
        return string
 
    def get_color_string(self, colors):
        if colors == "Start State":
            return colors
        
        string = ''
        for color in colors:
            if color == RED:
                string += "R "
            elif color == GREEN:
                string += "G "
            elif color == YELLOW:
                string += "Y "
            elif color == BLUE:
                string += "B "
        return string


# Takes in tiles and board to generate a DFA-like tree
# representing all the possible paths a solution might take
class Solution_Tree(object):
    def __init__(self, tiles, edges):
        self.root = Node()
        self.root.tile = "Start State"
        self.possible_tiles = self.get_all_tile_orientations(tiles)
        self.puzzle_edges = []
        for edge in edges:
            self.puzzle_edges.append(edge.get_color())
        self.solutions = []     # list of list of tiles representing all solutions
        self.generate_tree()
        self.generate_solutions()

    # Account for all possible placeable color combos taking rotations into account
    def get_all_tile_orientations(self, tiles):
        possible = []
        for tile in tiles:
            color = tile.get_color()
            possible.append(color)
            possible.append((color[1], color[2], color[3], color[0]))
            possible.append((color[2], color[3], color[0], color[1]))
            possible.append((color[3], color[0], color[1], color[2]))
        return possible

    # Return a node's children data given 3 or 4 edge colors
    def get_possible_children(self, edge_colors):
        children = [] 
        for possible in self.possible_tiles:
            check = list(possible)
            if len(edge_colors) == 3:
                check.pop(1)            # Don't care about the rightmost color
            if check == edge_colors and possible not in children:
                children.append(possible)
        return children

    def generate_tree(self):
        # Create tree in a depth-first manner
        stack = [] # Can simulate stack with pop() and append()
        stack.append(self.root)
    
        while len(stack) > 0:
            current_node = stack.pop()

            # If the node is at max depth, store it for later use in building solution
            if current_node.depth == len(self.puzzle_edges):
                self.solutions.append(current_node)
            
            if current_node.depth < len(self.puzzle_edges):
                # Get colors of possible children
                next_colors = list(self.puzzle_edges[current_node.depth])
                if 0 < current_node.depth < len(self.puzzle_edges):
                    next_colors.append(current_node.get_right_color())
                children = self.get_possible_children(next_colors)
            
                # Add as children to current node and push on stack
                for tile in children:
                    current_node.add_child(tile)
                for child in current_node.children:
                    stack.append(child)

    def generate_solutions(self):
        endNodes = self.solutions
        self.solutions = []
        for end in endNodes:
            solution = []
            child = end
            # Get solution via doubly-linked list
            while child.parent != None:
                # Creates tile with said colors for use of overloaded operator
                solution.append(Tile(10,10,10,child.tile))
                child = child.parent
            solution.reverse()
            self.solutions.append(solution)

class TwoStackPDA(object):
    def __init__(self, s1, s2, transitions, hist):
        self.stack1 = s1
        self.stack2 = s2
        self.transitions = transitions
        self.history = hist

    def can_take_transition(self, element1, element2):
        if self.stack1[-1] == element1 and self.stack2[-1] == element2:
            return True
        else:
            return False
    
    # Only called when can_take_transition returns true so has no internal checks
    def take_transition(self):
        i = self.stack1.pop()
        j = self.stack2.pop()
        self.history += '\ne, ' + str(i) + ', ' + str(j) + ' --> e, e'
    
    # Initialize the stacks by pushing a '$' onto each
    def initial_push(self):
        self.stack1.append('$')
        self.stack2.append('$')
        self.history += '\n' + 'e, e, e --> $, $'

    # Given how the solutions are fed in, this pushes a correct tile onto stack1
    # while the correct index of that tile is pushed onto stack2
    def push(self, tile):
        self.stack1.append(tile)
        self.stack2.append(len(self.stack1)-2)
        self.history += '\n' + str(tile) + ', e, e --> ' + str(tile) + ', ' + str(len(self.stack1)-2)

    def set_transitions(self, t):
        self.transitions = t

    # PDA reached reject, so print possible corrections
    def add_suggestions(self):
        self.history += '\n\nCould not take any more transitions from here -- Invalid Solution\n'
        self.history += '\nNot taking into account the transitions above, valid transitions at this point in the PDA are:'
        index = len(self.stack1)-2
        suggestions = Set()
        for t in self.transitions:
            if t[1] == index:
                suggestions.add('\ne, ' + str(t[0]) + ', ' + str(index) + ' --> e, e')
        for s in suggestions:
            self.history += s
            

# Somewhat represents the NPDA with all possible transitions contained in it for all solutions
class SolutionChecker(object):
    def __init__(self, userInput, solutions):
        self.initialPDA = TwoStackPDA([], [], [], "")
        self.initialPDA.initial_push()
        for tile in userInput:
            self.initialPDA.push(tile)

        self.transitions = []
        for sol in solutions:
            for i in range(0, len(sol)):
                self.transitions.append( (sol[i], i) )
        self.transitions.append( ('$', '$') )

        self.initialPDA.set_transitions(self.transitions)
        self.run_PDAs()

    def run_PDAs(self):
        dPDAs = []
        dPDAs.append(self.initialPDA)
        while len(dPDAs) > 0:
            updatedPDAs = []
            for pda in dPDAs:
                # If the stack is empty, accept state
                if len(pda.stack1) == 0:
                    print '\nPDA ACCEPTED:'
                    print pda.history
                    print '\nThe stack has been emptied -- Valid Solution'
                    return
                # See if any of the transitions can be taken, and if so, follow the path by creating another PDA object
                for transition in pda.transitions:
                    if pda.can_take_transition(transition[0], transition[1]):
                        newPDA = TwoStackPDA(list(pda.stack1), list(pda.stack2), pda.transitions, pda.history)
                        newPDA.take_transition()
                        updatedPDAs.append(newPDA)
            # If no transitions were taken at all, reject state
            if len(updatedPDAs) == 0:
                wrongPDAs = Set()
                for wrong in dPDAs:
                    wrong.add_suggestions()
                    wrongPDAs.add(wrong.history)
                for wrong in wrongPDAs:    
                    print '\nPDA REJECTED:'
                    print wrong
            dPDAs = list(updatedPDAs)
