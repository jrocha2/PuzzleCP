from objects import *

    #################################################################################
### For the purpose of this file, "tile" refers simply to the colors of a given tile ###
    #################################################################################

class Node(object):
    # Node with no parent/tile data is the root
    def __init__(self):
        self.tile = None
        self.children = []
        self.parent = None
        self.exhausted = False

    # Add a tile to current node's children pointing to it as parent 
    def add_child(self, tile):
        node = Node()
        node.tile = tile
        node.parent = self
        self.children.append(node)


class SolutionDFA(object):
    def __init__(self, tiles, edges):
        self.root = Node()
        self.possible_tiles = self.get_all_tile_orientations(tiles)
        self.puzzle_edges = edges

    # Account for all possible placeable color combos taking rotations into account
    def get_all_tile_orientations(tiles):
        possible = []
        for tile in tiles:
            color = tile.get_color()
            possible.append(color)
            possible.append((color[1], color[2], color[3], color[0]))
            possible.append((color[2], color[3], color[0], color[1]))
            possible.append((color[3], color[0], color[1], color[2]))
        return possible

    # Populate a node's children data given 3 or 4 edge colors
    def find_possible_children(self, edge_colors):
        children = [] 
        for possible in self.possible_tiles:
            check = possible
            if len(edge_colors) == 3:
                check.pop(1)            # Don't care about the rightmost color
            if check == edge_colors:
                children.append(possible)
        return children
