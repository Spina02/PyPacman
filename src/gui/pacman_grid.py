import json
import os

from src.configs import *
from src.sprites.pacman import Pacman
from src.sprites.ghosts import GhostManager
from src.utils.coord_utils import place_elements_offset, precompute_matrix_coords
from src.utils.draw_utils import draw_circle, draw_debug_rects, draw_rect

class PacmanGrid:
    def __init__(self, screen, game_state, pacman_pos = None):
        self.function_mapper = {
            "void": self.draw_void,
            "wall": self.draw_wall,
            "dot": self.draw_dot,
            "power": self.draw_power,
            "null": self.draw_void,
            "elec": self.draw_elec,
        }
        self._screen = screen
        self._game_state = game_state
        self._level_number = self._game_state.level
        self._pacman_pos = pacman_pos
        self.load_level(self._level_number)
        self.pacman = Pacman(
            self._screen,
            self._game_state,
            self._matrix,
            self._pacman_pos,
            (self.start_x, self.start_y)
        )
        self.ghost = GhostManager(
            self._screen,
            self._game_state,
            self._matrix,
            self.ghost_den,
            (self.start_x, self.start_y)
        )
        
    def get_json(self, path):
        with open(path) as fp:
            payload = json.load(fp)
        return payload

    def load_level(self, level_number):
        level_path = f"levels/level{level_number}.json"
        level_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "..", level_path))
        level_json = self.get_json(level_abs_path)
        num_rows = level_json["num_rows"]
        num_cols = level_json["num_cols"]
        self.ghost_den = level_json['ghost_den']
        self._matrix = level_json["matrix"]
        self._game_state.set_level_matrix(self._matrix)
        if self._pacman_pos is None:
            self._pacman_pos = level_json["pacman_start"]
        self.elec_pos = level_json['elec']
        self.mode_change_times = level_json['scatter_times']
        self.power_up_time = (level_json['power_up_time'] * self._game_state.fps // 1000)
        self._game_state.scared_time = self.power_up_time
        self._game_state.mode_change_events = self.mode_change_times
 
        self.start_x, self.start_y = place_elements_offset(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            CELL_SIZE[0] * num_cols,
            CELL_SIZE[0] * num_rows,
            0.5,
            0.5,
        )
        self._game_state.start_pos = (self.start_x, self.start_y)
        self._coord_matrix = precompute_matrix_coords(
            self.start_x, self.start_y, CELL_SIZE[0], num_rows, num_cols
        )
        self.num_rows = num_rows
        self.num_cols = num_cols

    def draw_void(self, **kwargs):
        pass

    def draw_wall(self, **kwargs):
        draw_rect(
            kwargs["x"],
            kwargs["y"],
            kwargs["w"],
            kwargs["h"],
            self._screen,
            Colors.WALL_BLUE,
        )

    def draw_dot(self, **kwargs):
        dot_x = kwargs["x"] + kwargs["w"]
        dot_y = kwargs["y"] + kwargs["h"]
        draw_rect(dot_x, dot_y, 5, 5, self._screen, Colors.WHITE)

    def draw_power(self, **kwargs):
        circle_x = kwargs["x"] + kwargs["w"]
        circle_y = kwargs["y"] + kwargs["h"]
        draw_circle(circle_x, circle_y, 7, self._screen, Colors.YELLOW)

    def draw_elec(self, **kwargs):
        draw_rect(kwargs["x"], kwargs["y"], kwargs["w"], 1, self._screen, Colors.RED)

    def draw_level(self):
        curr_x, curr_y = self.start_x, self.start_y
        for row in self._matrix:
            for col in row:
                draw_func = self.function_mapper[col]
                draw_func(x=curr_x, y=curr_y, w=CELL_SIZE[0], h=CELL_SIZE[0])
                curr_x += CELL_SIZE[0]
            curr_x = self.start_x
            curr_y += CELL_SIZE[0]

    def reset_stage(self):
        self.pacman = Pacman(
            self._screen,
            self._game_state,
            self._matrix,
            self._pacman_pos,
            (self.start_x, self.start_y)
        )
        self.ghost = GhostManager(
            self._screen,
            self._game_state,
            self._matrix,
            self.ghost_den,
            (self.start_x, self.start_y)
        )
        
    def draw_outliners(self):
        draw_debug_rects(
            self.start_x, self.start_y, 128, 140, 5, Colors.GREEN, self._screen
        )
        draw_debug_rects(
            self.start_x,
            self.start_y,
            self.num_rows,
            self.num_cols,
            CELL_SIZE[0],
            Colors.BLUE,
            self._screen,
        )
