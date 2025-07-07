from src.configs import *
from src.gui.pacman_grid import *
from src.gui.score_screen import ScoreScreen

from pygame.time import wait

class ScreenManager:
    def __init__(self, screen, game_state, all_sprites, pacman_pos = None):
        self._screen = screen
        self._game_state = game_state
        self.all_sprites = all_sprites
        self.pacman_pos = pacman_pos
        self.pacman = PacmanGrid(screen, game_state, pacman_pos)
        self.score_screen = ScoreScreen(self._screen, self._game_state)
        self.all_sprites.add(self.pacman.pacman)
        for ghost in self.pacman.ghost.ghosts_list:
            self.all_sprites.add(ghost)

    def pacman_dead_reset(self):
        if self._game_state.is_pacman_dead:
            self._game_state.is_pacman_dead = False
            self._game_state.direction = ""
            self._game_state.pacman_direction = None
            self.all_sprites.empty()
            self.pacman.reset_stage()
            self.all_sprites.add(self.pacman.pacman)
            for ghost in self.pacman.ghost.ghosts_list:
                self.all_sprites.add(ghost)
    
    def check_level_complete(self):
        if self._game_state.level_complete:
            wait(2000)
            self.all_sprites.empty()
            self.pacman = PacmanGrid(self._screen, self._game_state, self.pacman_pos)
            self.score_screen = ScoreScreen(self._screen, self._game_state)
            self.all_sprites.add(self.pacman.pacman)
            for ghost in self.pacman.ghost.ghosts_list:
                self.all_sprites.add(ghost)
            self._game_state.level_complete = False

    def draw_screens(self):
        self.pacman.draw_level()
        self.pacman_dead_reset()
        self.score_screen.draw_scores()
        self.check_level_complete()
