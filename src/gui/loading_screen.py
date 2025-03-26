import os
from src.configs import loading_screen_gif
from pygame import image, transform

class LoadingScreen: 
    def __init__(self, screen): 
        self.screen = screen # Calcola il percorso assoluto dell'asset partendo dalla cartella del modulo 
        this_dir = os.path.dirname(loading_screen_gif) # loading_screen_gif è definito in src/configs.py (es. "assets/other/loading.gif") 
        asset_path = os.path.join(this_dir, "..", loading_screen_gif) 
        asset_path = os.path.abspath(asset_path) 
        self.loading_image = image.load(asset_path) # Carica l'immagine 
        self.loading_image = transform.scale(self.loading_image, (192, 192))

def draw_loading(self):
    self.screen.blit(self.loading_image, (500, 500))
