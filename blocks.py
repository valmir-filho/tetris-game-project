from block import Block  # Importing the Block class.
from position import Position  # Importing the Position class.


# Class to represent the L-shaped block (typically in Tetris).
class LBlock(Block):


    # Constructor to initialize an L-shaped block.
    def __init__(self):
        super().__init__(id=1)  # Calling the parent constructor with block ID 1.
        # Defining the cells for each rotation state of the L-shaped block.
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # Moves the block to an initial starting position.


# Class to represent the J-shaped block.
class JBlock(Block):


    # Constructor to initialize a J-shaped block.
    def __init__(self):
        super().__init__(id=2)  # Block ID 2.
        # Defining the cells for each rotation state of the J-shaped block.
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)  # Initial position.


# Class to represent the I-shaped block (the long piece).
class IBlock(Block):


    # Constructor to initialize an I-shaped block.
    def __init__(self):
        super().__init__(id=3)  # Block ID 3.
        # Defining the cells for each rotation state of the I-shaped block.
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)  # Moves the block slightly higher at the start.


# Class to represent the O-shaped block (the square piece).
class OBlock(Block):


    # Constructor to initialize an O-shaped block.
    def __init__(self):
        super().__init__(id=4)  # Block ID 4.
        # The O-shaped block doesn't rotate, so there's only one rotation state.
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)  # Moves the block to the starting position.


# Class to represent the S-shaped block.
class SBlock(Block):


    # Constructor to initialize an S-shaped block.
    def __init__(self):
        super().__init__(id=5)  # Block ID 5.
        # Defining the cells for each rotation state of the S-shaped block.
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # Initial position.


# Class to represent the T-shaped block.
class TBlock(Block):


    # Constructor to initialize a T-shaped block.
    def __init__(self):
        super().__init__(id=6)  # Block ID 6.
        # Defining the cells for each rotation state of the T-shaped block.
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # Initial position.


# Class to represent the Z-shaped block.
class ZBlock(Block):


    # Constructor to initialize a Z-shaped block.
    def __init__(self):
        super().__init__(id=7)  # Block ID 7.
        # Defining the cells for each rotation state of the Z-shaped block.
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)  # Initial position.
