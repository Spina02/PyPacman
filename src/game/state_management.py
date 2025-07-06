import numpy as np

from src.configs import DOT_POINT

class GameState:
    def __init__(self, level = 1):
        self._sound_enabled = True
        self._start_pos = None
        self.__level = level
        self.__running = True
        self.__fps = 60
        self.__direction = ""
        self.__current_time = None
        self.__pacman_rect = None
        self.__ghost_pos = {}
        self.__is_loaded = False
        self.__is_pacman_powered = 0
        self._ghost_mode = 'chase'
        self._mode_change_events = None
        self.__current_mode_index = 0
        self.__mode_timer = 0
        self._custom_event = None
        self._pacman_direction = None
        self._blinky_matrix_pos = None
        self._scared_time = None
        self._scared_ghosts = [False, False, False, False]
        self._power_up_event = None
        self._power_event_trigger_time = None
        self._is_pacman_dead = False
        self._highscore = 0
        self._mins_played = 0
        self._points = -DOT_POINT
        self._level_complete = False
        self.level_matrix_np = None
        self._step_count = 0
        self.tile_encoding = {
            "wall": 0,
            "dot": 1,
            "power": 2,
            "void": 3,
            "elec": 4
        }
        self.ghost_encoding = {
            "blinky": 0,
            "pinky": 1,
            "inky": 2,
            "clyde": 3
        }
        self.tile_decoding = {v: k for k, v in self.tile_encoding.items()}
        self._no_ghosts = {name : False for name in self.ghost_encoding.keys()}

    @property
    def level_complete(self):
        return self._level_complete
    @level_complete.setter
    def level_complete(self, val):
        self._level_complete = val

    @property
    def points(self):
        return self._points
    @points.setter
    def points(self, val):
        self._points = val

    @property
    def highscore(self):
        return self._highscore
    @highscore.setter
    def highscore(self, val):
        self._highscore = val
    
    @property
    def mins_played(self):
        return self._mins_played
    @mins_played.setter
    def mins_played(self, val):
        self._mins_played = val

    @property
    def is_pacman_dead(self):
        return self._is_pacman_dead
    @is_pacman_dead.setter
    def is_pacman_dead(self, val):
        self._is_pacman_dead = val

    @property
    def power_event_trigger_time(self):
        return self._power_event_trigger_time
    @power_event_trigger_time.setter
    def power_event_trigger_time(self, val):
        self._power_event_trigger_time = val

    @property
    def power_up_event(self):
        return self._power_up_event
    @power_up_event.setter
    def power_up_event(self, val):
        self._power_up_event = val

    @property
    def scared_time(self):
        return self._scared_time
    @scared_time.setter
    def scared_time(self, val):
        self._scared_time = val

    @property
    def blinky_matrix_pos(self):
        return self._blinky_matrix_pos
    @blinky_matrix_pos.setter
    def blinky_matrix_pos(self, val):
        self._blinky_matrix_pos = val

    @property
    def pacman_direction(self):
        return self._pacman_direction
    @pacman_direction.setter
    def pacman_direction(self, val):
        self._pacman_direction = val

    @property
    def custom_event(self):
        return self._custom_event
    @custom_event.setter
    def custom_event(self, val):
        self._custom_event = val

    @property
    def mode_change_events(self):
        if self.__current_mode_index >= len(self._mode_change_events):
            curr_event = self._mode_change_events[-1]
        else:
            curr_event = self._mode_change_events[self.__current_mode_index]
            self.__current_mode_index += 1
        return curr_event
    @mode_change_events.setter
    def mode_change_events(self, val):
        self._mode_change_events = val

    @property
    def ghost_mode(self):
        return self._ghost_mode
    @ghost_mode.setter
    def ghost_mode(self, value):
        if value not in ['scatter', 'chase', 'scared']:
            raise ValueError("Only scatter, scared or chase modes are available")
        self._ghost_mode = value

    @property
    def is_pacman_powered(self):
        return self.__is_pacman_powered
    @is_pacman_powered.setter
    def is_pacman_powered(self, val):
        self.__is_pacman_powered = val
        
    @property
    def is_loaded(self):
        return self.__is_loaded

    def get_ghost_pos(self, name):
        return self.__ghost_pos.get(name)
    
    def set_ghost_pos(self, name, val):
        self.__ghost_pos[name] = val
        
    @property
    def ghosts(self):
        return self.__ghost_pos

    @property
    def pacman_rect(self):
        return self.__pacman_rect
    @pacman_rect.setter
    def pacman_rect(self, rect):
        self.__pacman_rect = rect

    @property
    def current_time(self):
        return self.__current_time
    @current_time.setter
    def current_time(self, val):
        self.__current_time = val

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, value):
        if value not in ["r", "l", "u", "d", ""]:
            raise ValueError("Unknown direction")
        self.__direction = value

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def running(self):
        return self.__running
    @running.setter
    def running(self, value):
        self.__running = value

    @property
    def fps(self):
        return self.__fps
    @fps.setter
    def fps(self, value):
        self.__fps = value

    #? -------------------------------------------
    #?             Custom properties
    #? -------------------------------------------
    
    @property
    def start_pos(self):
        return self._start_pos
    @start_pos.setter
    def start_pos(self, pos):
        self._start_pos = pos

    @property
    def step_count(self):
        return self._step_count
    @step_count.setter
    def step_count(self, val):
        self._step_count = val
        
    @property
    def mode_change_times(self):
        return self._mode_change_events
    
    @property
    def current_mode_index(self):
        return self.__current_mode_index
    
    @property
    def mode_timer(self):
        timer =  self.__mode_timer
        self.__mode_timer -= 1
        return timer
    @mode_timer.setter
    def mode_timer(self, val):
        self.__mode_timer = val
        
    @property
    def sound_enabled(self):
        return self._sound_enabled
    @sound_enabled.setter
    def sound_enabled(self, val):
        self._sound_enabled = val
        
    @property
    def scared_ghosts(self):
        return self._scared_ghosts
    @scared_ghosts.setter
    def scared_ghosts(self, val):
        self._scared_ghosts = val
        
    @property
    def no_ghosts(self):
        return self._no_ghosts
    @no_ghosts.setter
    def no_ghosts(self, val):
        self._no_ghosts = val
    
    #? -------------------------------------------
    #?              Custom methods
    #? -------------------------------------------

    def set_level_matrix(self, matrix_list):
        """
        Set the level matrix as a numpy array
        """
        # Convert the matrix to a numpy array
        vectorize_encode = np.vectorize(lambda tile: self.tile_encoding.get(tile, -1))
        self.level_matrix_np = vectorize_encode(np.array(matrix_list))
    
    def update_tile(self, row, col, new_tile):
        """
        Update a tile in the level matrix
        """
        self.level_matrix_np[row, col] = self.tile_encoding.get(new_tile, -1)