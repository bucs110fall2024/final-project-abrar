import pygame
import random
import os

class SoundManager:
    def __init__(self, assets_folder):
        """Initialize the sound manager and load sound effects."""
        self.sounds = []
        for filename in os.listdir(assets_folder):
            if filename.endswith(".ogg"):
                self.sounds.append(pygame.mixer.Sound(os.path.join(assets_folder, filename)))

    def play_random_sound(self):
        """Play a random sound from the loaded sounds."""
        if self.sounds:
            random.choice(self.sounds).play()
