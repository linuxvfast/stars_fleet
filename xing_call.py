# -*- coding:utf-8 -*-
import pygame
from setting_xing import Settings_test
import game_xing as gx
from pygame.sprite import Group
from xing import Stars

def run_game():
    pygame.init()
    set_screen = Settings_test()
    screen = pygame.display.set_mode((set_screen.screen_width,set_screen.screen_height))
    pygame.display.set_caption('Blues Screen')

    #创建星星
    stars_numbers = Group()
    gx.create_stars_fleet(set_screen,screen,stars_numbers)
    while True:
        gx.check_events(set_screen,screen)
        gx.update_screen(set_screen,screen,stars_numbers)
run_game()

