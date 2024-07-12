class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (130, 230, 230)

        #Ship settings
        self.ship_speed_factor = 1.5
        self.ships_limit = 3

        #Bullet settings
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        """alien settings"""

        ##self.alien_speed_factor = 1
        
        self.fleet_drop_speed = 2

        # fleet_direction of 1 represents right, -1 = left
        ##self.fleet_direction = 1

        self.speedup_scale = 1.1
        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction of 1 represents right, -1 = left
        self.fleet_direction = 1
        #scoring
        self.alien_points = 50
        

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_ponts = int(self.alien_points * self.score_scale)
        print(self.alien_points)


