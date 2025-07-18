from pygame import (K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT)

class EventHandler:
    def __init__(self, screen, game_state):
        self._screen = screen
        self._game_screen = game_state

    def pygame_quit(self):
        self._game_screen.running = False

    def key_bindings(self, key):
        if key == K_LEFT:
            self._game_screen.direction = "l"
        elif key == K_RIGHT:
            self._game_screen.direction = "r"
        elif key == K_UP:
            self._game_screen.direction = "u"
        elif key == K_DOWN:
            self._game_screen.direction = "d"
            
    def check_frame_events(self):
        """
        Check for events that should happen based on frame count rather than real time
        """
        # Check for ghost mode changes
        if self._game_screen.mode_timer < 0:
            # Time to change modes
            next_mode = 'scatter' if self._game_screen.ghost_mode == 'chase' else 'chase'
            self._game_screen.ghost_mode = next_mode
            # Update the start time for the next mode
            self._game_screen.mode_timer = self._game_screen.mode_change_events * self._game_screen.fps

        # Check for power-up expiration
        if self._game_screen.is_pacman_powered:
            self._game_screen.is_pacman_powered -= 1
            # power_duration = self._game_screen.scared_time
            # if self._game_screen.step_count >= self._game_screen.power_event_trigger_time + power_duration:
        else:
            self._game_screen.is_pacman_powered = 0

    def handle_events(self, event, manual=True):
        if event.type == QUIT:
            self.pygame_quit()
        if manual and event.type == KEYDOWN:
            self.key_bindings(event.key)
