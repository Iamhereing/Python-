import sys

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group # 导入编组功能

def run_game(): # 初始化游戏并创建一个屏幕对象
    pygame.init() # 初始化背景设置
    ai_settings = Settings() # 将矢量图形设置代入基本设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)) # 调用一个1200×800的显示窗口
    pygame.display.set_caption("Alien Invasion") # 设置这个游戏的标题

    stats = GameStats(ai_settings)  # 创建一个用于存储游戏统计信息的实例
    ship = Ship(ai_settings,screen) # 创建一艘飞船
    bullets = Group() # 创建一个用于存储子弹的编组
    aliens = Group() # 创建一个用于存储外星人的编组

    gf.create_fleet(ai_settings, screen, ship, aliens) # 创建外星人群

    while True: # 开始游戏的主循环

        gf.check_events(ai_settings, screen, ship, bullets) # 响应事件的函数
        if stats.game_active:
            ship.update()  # 飞船的按键控制情况
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)  # 更新外星人和子弹的情况
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)  # 更新外星人群

        gf.update_screen(ai_settings, screen, ship, aliens, bullets) # 矢量图形
                                             # 的基本设置， 屏幕， 飞船,子弹，外星人




run_game() # 运行游戏，初始化游戏并开始主循环