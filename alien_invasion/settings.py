class Settings:
    """A class to store all settings for Alien invasion"""

    def __init__(self):
        """Initialize the game's static setting"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 100, 255)

        # Bullet settings
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3.0

        # Alien settings
        self.fleet_drop_speed = 10.0
        # fleet_direction of 1 represents right; -1 represents left

        self.fleet_direction = 1
        self.shiplimit = 3.0

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increased
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 7.0
        self.bullet_speed = 12.0
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right while -1 is ;lelf
        self.sleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
    
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)