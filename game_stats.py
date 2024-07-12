class GameStats():
    """Track statistis for alien invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien invasion in an active state
        self.game_active = False
        self.score = 0

    
    def reset_stats(self):
        """Initialize statistics that can change during the game""" 
        self.ships_left = self.ai_settings.ships_limit
        
    