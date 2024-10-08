#imorting the game library
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    
    #Initialize game and reate a screen object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")


    #Make play button
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store game statistics and create a score board
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #make ship
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    #Make a group of aliens
    aliens = Group()

    #create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    


    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button) 
             
        
        
run_game()



