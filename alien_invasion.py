import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():

    #Initialize the game and create a screen object

    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create a spaceship

    ship=Ship(ai_settings,screen)

    #Create an alien

    alien = Alien(ai_settings, screen)

    #Create groups of bullets

    bullets=Group()

    #The main loop of game

    while True:

        #check mouse and keyboard event
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


        

run_game()
