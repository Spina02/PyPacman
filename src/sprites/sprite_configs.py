import os

# Base directory for assets
def get_absolute_path(relative_path):
    """Convert a relative asset path to an absolute path"""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base_dir, relative_path)

# Apply the function to all paths
PACMAN_PATHS = {
    "left": [
        get_absolute_path("assets/pacman-left/1.png"),
        get_absolute_path("assets/pacman-left/2.png"),
        get_absolute_path("assets/pacman-left/3.png"),
    ],
    "right": [
        get_absolute_path("assets/pacman-right/1.png"),
        get_absolute_path("assets/pacman-right/2.png"),
        get_absolute_path("assets/pacman-right/3.png"),
    ],
    "up": [
        get_absolute_path("assets/pacman-up/1.png"),
        get_absolute_path("assets/pacman-up/2.png"),
        get_absolute_path("assets/pacman-up/3.png"),
    ],
    "down": [
        get_absolute_path("assets/pacman-down/1.png"),
        get_absolute_path("assets/pacman-down/2.png"),
        get_absolute_path("assets/pacman-down/3.png"),
    ],
}

GHOST_PATHS = {
    "inky": [get_absolute_path("assets/ghosts/inky.png")],
    "pinky": [get_absolute_path("assets/ghosts/pinky.png")],
    "blinky": [get_absolute_path("assets/ghosts/blinky.png")],
    "clyde": [get_absolute_path("assets/ghosts/clyde.png")],
    "blue": [get_absolute_path("assets/ghosts/blue_ghost.png")]
}
