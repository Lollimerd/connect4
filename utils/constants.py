# constants.py - Stores game constants and configuration

# Board dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)

# Screen dimensions
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE  # Extra row for dropping pieces

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Player tokens
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

# Game states
PLAYING = 0
PLAYER_1_WIN = 1
PLAYER_2_WIN = 2
TIE = 3