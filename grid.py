from colors import Colors
import pygame


class Grid:
    

    def __init__(self):
        # Initialize grid size and colors.
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        # Create a 2D list to represent the grid, initially filled with 0s (empty).
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()  # Get color mapping for cells


    # Prints the grid values to the console (for debugging purposes).
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()


    # Checks if a given row and column are within the grid boundaries.
    def is_inside(self, row, column):
        if 0 <= row < self.num_rows and 0 <= column < self.num_cols:
            return True
        return False


    # Checks if a cell at a specific position is empty (value is 0).
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False


    # Checks if a row is full (no empty cells).
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True


    # Clears a row by setting all its cells to 0.
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0


    # Moves a row down by the specified number of rows.
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0


    # Clears all full rows and moves down any rows above them.
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):  # Start from the bottom row.
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                # Move non-full rows down by the number of completed rows.
                self.move_row_down(row, completed)
        return completed


    # Resets the grid, making all cells empty.
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0


    # Draws the grid on the screen.
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Create a rectangle for each cell with a small padding for visual separation.
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                # Draw the cell using the appropriate color based on its value.
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
