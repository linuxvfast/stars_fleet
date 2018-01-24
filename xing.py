#!-*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Stars(Sprite):
    '''表示星星的类'''
    def __init__(self,set_screen,screen):
        '''初始化外星人并设置起始的位置'''
        super().__init__()
        self.screen = screen
        self.set_screen = set_screen

        #加载星星的图像，并设置rect属性
        self.image = pygame.image.load('images/stars.bmp')
        self.rect = self.image.get_rect()

        #每个星星最初都放在屏幕左上角
        self.rect.x = 5
        self.rect.y = 5

        #放置外星人的位置
        self.x = float(self.rect.x)

    def draw(self):
        '''在屏幕画星星'''
        self.screen.blit(self.image,self.rect)


