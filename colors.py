# Class to hold a set of predefined colors as RGB tuples.
class Colors:
    # Defining various colors as RGB tuples.
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)  # A common color often used as a background or highlight.
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)


    # Class method to return a list of certain block colors (likely for Tetris blocks or a similar game).
    @classmethod
    def get_cell_colors(cls):
        # Returns a list of colors (without white, dark_blue, and light_blue).
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
