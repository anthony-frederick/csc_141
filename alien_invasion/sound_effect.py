import pygame

class SoundManager:
    """A class to manage sound effects in the game"""

    def __init__(self):
        """Initialize the sound manager and load sound files"""
        pygame.mixer.init()  # Ensure the mixer is initialized
        self.sounds = {}

    def load_sound(self, sound_name, file_path):
        """Load a sound file and add it to the sounds dictionary"""
        try:
            sound = pygame.mixer.Sound(file_path)
            self.sounds[sound_name] = sound
        except pygame.error as e:
            print(f"Error loading sound {sound_name} from {file_path}: {e}")

    def play_sound(self, sound_name):
        """Play a sound by its name"""
        sound = self.sounds.get(sound_name)
        if sound:
            sound.play()
        else:
            print(f"Sound '{sound_name}' not found.")
    
    def set_volume(self, sound_name, volume):
        """Set the volume for a specific sound"""
        sound = self.sounds.get(sound_name)
        if sound:
            sound.set_volume(volume)
        else:
            print(f"Sound '{sound_name}' not found.")