import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen # 加载屏幕
        self.ai_settings = ai_settings # 加载基本设置属性

        self.image = pygame.image.load('images/alien.bmp') # 加载外星人图片
        self.rect = self.image.get_rect() # 加载外星人的矩形框

        self.rect.x = self.rect.width  # 矩形的宽度等于X值
        self.rect.y = self.rect.height # 矩形的高度等于Y值
         # 意思就是如果矩形的宽高是5和3,那么矩形的坐标就是（5,3）
         #  即外星人最初在屏幕左上角


        self.x = float(self.rect.x) # 使X值可以是小数值

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 将外星人加载在屏幕上

    def check_edges(self): # 检查是否靠近边缘的类
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: # 如果外星人矩形右边缘大于屏幕右边缘
            return True
        elif self.rect.left <= 0:  # 如果外星人矩形左边缘小于屏幕左边缘
            return True

    def update(self): # 更新
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)# 以初始速度向左或向右移动
        self.rect.x = self.x # 外星人矩形X值=外星人X值
