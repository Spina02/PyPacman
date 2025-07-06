class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WALL = (112, 167, 255)
    YELLOW = (252, 186, 3)
    WALL_BLUE = (24, 24, 217)


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
CELL_SIZE = (20, 20)
NUM_ROWS = 30
NUM_COLS = 33
PACMAN = (32, 32)
GHOSTS = (32, 32)
PACMAN_SPEED = 4
GHOST_SPEED_FAST = 4
GHOST_SPEED_SLOW = 3.5
GHOST_NORMAL_DELAY = 5000

DOT_POINT = 10
POWER_POINT = 15
GHOST_POINT = 25
LEVEL_COMP_POINT = 80

GHOST_DELAYS = {
    "inky": 15000,
    "pinky": 10000,
    "blinky": 5000,
    "clyde": 20000,
    "blue": 0
}
GHOST_TARGET_CHANGE = {
    "inky": 10,
    "pinky": 8,
    "blinky": 6,
    "clyde": 7,
    "blue": 7
}
GHOST_SCATTER_TARGETS = {
    'blinky': (0, 30),
    "pinky": (0, 0),
    "inky": (31, 0),
    "clyde": (31, 30)
}