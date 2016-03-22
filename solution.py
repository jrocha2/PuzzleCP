from objects import *
from collections import deque

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

    def __str__(self, level=0):
        string = "\t"*level+ str(level) + "-->" + str(self.tile)+"\n"
        for child in self.children:
            string += child.__str__(level+1)
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
        self.generate_tree()

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
