# -*- coding:utf-8 -*-
import pygame
from settings_test import Settings_test
from ship_test import Ship_Test
import game_test as gt
from pygame.sprite import Group
def run_game():
    pygame.init()
    setscreen = Settings_test()
    screen = pygame.display.set_mode((setscreen.screen_width,setscreen.screen_height))
    pygame.display.set_caption('Blues Screen')

    #新建飞船
    xing = Ship_Test(setscreen,screen)

    #存放子弹的编组
    bullets = Group()
    while True:
        gt.check_events(setscreen,screen,xing,bullets)
        xing.update()
        gt.update_bullets(setscreen,bullets)
        gt.update_screen(setscreen,screen,xing,bullets)
run_game()

