# -*- coding:utf-8 -*-
import sys,pygame
from xing import Stars
def check_keydown_events(event,set_screen,screen):
#     if event.key == pygame.K_RIGHT:
#         xing.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         xing.moving_left = True
#     elif event.key == pygame.K_DOWN:
#         xing.moving_down = True
#     elif event.key == pygame.K_UP:
#         xing.moving_up = True
#     elif event.key == pygame.K_SPACE:
#         fire(setscreen,screen,xing,bullets)
    if event.key == pygame.K_q:
        sys.exit()
# def check_keyup_events(event,xing):
#     if event.key == pygame.K_RIGHT:
#         xing.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         xing.moving_left = False
#     elif event.key == pygame.K_DOWN:
#         xing.moving_down = False
#     elif event.key == pygame.K_UP:
#         xing.moving_up = False

def check_events(set_screen,screen):
    '''监控鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,set_screen,screen)
        # elif event.type == pygame.KEYUP:
        #     check_keyup_events(event,xing)

def update_screen(set_screen,screen,stars):
    '''更新屏幕图像，显示新屏幕图像'''
    # 每次循环都重新绘制屏幕
    screen.fill(set_screen.bg_color_white)   #屏幕填充颜色
    stars.draw(screen)
    # 让最新绘制的屏幕可见
    pygame.display.flip()

def create_stars_fleet(set_screen,screen,stars_numbers):
    '''创建星星，计算一行中的个数'''
    stars = Stars(set_screen, screen)
    stars_width = stars.rect.width
    stars_height = stars.rect.height
    stars_number_x = get_stars_number_x(set_screen,stars_width)
    number_rows = get_number_rows(set_screen,stars_height)
    # 创建星星组
    for number_row in range(number_rows):
        for number in range(stars_number_x):
            create_stars(set_screen, screen,number,stars_numbers,number_row,stars_height)

def get_stars_number_x(set_screen,stars_width):
    '''计算一行中可以放星星的个数'''
    # x轴有效的长度(10为屏幕的两边间隔)
    available_space_x = set_screen.screen_width - 10
    # x轴可以放置的星星个数
    stars_number_x = int(available_space_x / (5 + stars_width))
    return stars_number_x

def create_stars(set_screen, screen,number,stars_numbers,number_row,stars_height):
    # 创建星星并加入当前的行
    stars = Stars(set_screen, screen)
    stars_width = stars.rect.width
    stars.x = 5 + (5 + stars_width) * number
    stars.rect.x = stars.x
    stars.rect.y = 5 + stars_height * number_row
    stars_numbers.add(stars)

def get_number_rows(set_screen,stars_height):
    '''计算容纳星星的行数'''
    available_space_y = set_screen.screen_height
    number_rows = int(available_space_y / (5 + stars_height))
    return  number_rows