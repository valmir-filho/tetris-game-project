import pygame
from colors import Colors  # Importing the Colors class from the colors module.
from position import Position  # Importing the Position class from the position module.


# Class to represent a Block, which is part of a game, likely a Tetris-like game.
class Block:


    # Constructor to initialize a Block object.
    def __init__(self, id):
        self.id = id  # Each block has a unique id.
        self.cells = {}  # A dictionary to store the block's cell positions for different rotation states.
        self.cell_size = 30  # Size of each cell in the block.
        self.row_offset = 0  # Row offset to move the block vertically.
        self.column_offset = 0  # Column offset to move the block horizontally.
        self.rotation_state = 0  # Current rotation state (which way the block is rotated).
        self.colors = Colors.get_cell_colors()  # Getting the block's color using the Colors class.


    # Method to move the block by adjusting the row and column offsets.
    def move(self, rows, columns):
        self.row_offset += rows  # Moves the block by a certain number of rows.
        self.column_offset += columns  # Moves the block by a certain number of columns.


    # Method to get the current positions of the block's cells after moving.
    def get_cell_positions(self):
        # Get the tiles (positions) of the block in the current rotation state.
        tiles = self.cells[self.rotation_state]
        moved_tiles = []  # A list to store the adjusted positions.
        # Adjust the positions based on the current row and column offsets.
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)  # Add the new position to the list.
        return moved_tiles  # Return the adjusted cell positions.


    # Method to rotate the block to the next rotation state.
    def rotate(self):
        self.rotation_state += 1  # Increment the rotation state to the next.
        # If the rotation state exceeds the available states, reset to the first state.
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0


    # Method to undo the last rotation (go back to the previous rotation state).
    def undo_rotation(self):
        self.rotation_state -= 1  # Decrement the rotation state to the previous one.
        # If the rotation state is less than 0, set it to the last state.
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1


    # Method to draw the block on the screen.
    def draw(self, screen, offset_x, offset_y):
        # Get the current positions of the block's cells.
        tiles = self.get_cell_positions()
        # Loop through each tile (cell) and draw it on the screen.
        for tile in tiles:
            # Create a rectangle for each tile based on its position and size.
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            # Draw the rectangle on the screen with the block's color.
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
