import pygame
import random

class StarryBackground:
    """A class to create a starry background with moving white squares"""

    def __init__(self, ai_game):
        """Initialize the background and set up resources"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # List to store star positions
        self.stars = pygame.sprite.Group()

        # Initialize stars
        self._create_stars()

    def _create_stars(self):
        """Create random stars that will move down the screen"""
        num_stars = 100  # Number of stars to generate
        for _ in range(num_stars):
            star = Star(self)
            self.stars.add(star)
            print(f"Star created at position: ({star.rect.x}, {star.rect.y})")  # Debug line

    def update(self):
        """Update the position of each star to simulate falling"""
        for star in self.stars.sprites():
            star.update()
            # If the star moves off the screen, reset it to the top
            if star.rect.top >= self.settings.screen_height:
                star.reset_position()

    def draw(self):
        """Draw all stars onto the screen"""
        for star in self.stars.sprites():
            star.draw()

class Star(pygame.sprite.Sprite):
    """A class to represent a single star"""

    def __init__(self, starry_background):
        """Initialize the star and set its starting position"""
        super().__init__()
        self.screen = starry_background.screen
        self.settings = starry_background.settings

        # Set random position and size
        self.x = random.randint(0, self.settings.screen_width)
        self.y = random.randint(-self.settings.screen_height, 0)
        self.size = (5)

        # Create a rectangle for the star
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

        # Set a random speed for the star (falling speed)
        self.speed = random.randint(5, 7)

        print(f"Star initialized at position: ({self.rect.x}, {self.rect.y})")  # Debug line

    def update(self):
        """Move the star down the screen"""
        self.rect.y += self.speed

    def reset_position(self):
        """Reset the position of the star to the top"""
        self.rect.y = -self.size  # Reset to just above the screen
        self.rect.x = random.randint(0, self.settings.screen_width)  # Random x position again
        self.speed = random.randint(5, 7)  # Assign a random speed again

    def draw(self):
        """Draw the star onto the screen"""
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)  # White star
