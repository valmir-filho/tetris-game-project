from blocks import *  # Importing all block types (IBlock, JBlock, etc.).
from grid import Grid
import random
import pygame


class Game:
    

    def __init__(self):
        # Initialize game elements.
        self.grid = Grid()  # Game grid.
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # All possible block types.
        self.current_block = self.get_random_block()  # Current block.
        self.next_block = self.get_random_block()  # Next block in queue.
        self.game_over = False
        self.score = 0
        # Load sound effects.
        self.rotate_sound = pygame.mixer.Sound("Python-Tetris-Game-Pygame-main/assets/sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Python-Tetris-Game-Pygame-main/assets/sounds/clear.ogg")
        # Load and start background music.
        pygame.mixer.music.load("Python-Tetris-Game-Pygame-main/assets/sounds/music.ogg")
        pygame.mixer.music.play(-1)  # Loop indefinitely.


    # Update score based on the number of lines cleared and movement points.
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points


    # Randomly selects a block from the available ones and removes it from the list.
    def get_random_block(self):
        if len(self.blocks) == 0:
            # Reset block pool if empty.
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block


    # Move block left.
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)  # Undo move if invalid.


    # Move block right.
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)  # Undo move if invalid.


    # Move block down.
    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)  # Undo move if invalid.
            self.lock_block()


    # Lock block into the grid when it can't move down anymore.
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            # Update the grid with the block's position.
            self.grid.grid[position.row][position.column] = self.current_block.id
        # Replace current block with next block.
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        # Clear full rows and update score.
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        # Check if game over.
        if not self.block_fits():
            self.game_over = True


    # Reset game state.
    def reset(self):
        self.grid.reset()  # Reset the grid.
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Reset block list.
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0


    # Check if current block fits in its current position.
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True


    # Rotate block, checking if it fits inside the grid and doesn't overlap.
    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()  # Undo rotation if invalid.
        else:
            self.rotate_sound.play()


    # Check if the block is within the grid boundaries.
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True


    # Draw the current block and the next block on the screen.
    def draw(self, screen):
        self.grid.draw(screen)  # Draw the grid.
        self.current_block.draw(screen, 11, 11)  # Draw the current block.
        # Draw the next block in a specific position based on its type.
        if self.next_block.id == 3:  # IBlock
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:  # OBlock
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
