import pygame

class Ship(): # 关于飞船设置的类

    def __init__(self, ai_settings, screen): #设置初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp') # 加载飞船图像
        self.rect = self.image.get_rect() # 根据飞船图像获得的一个矩形框，即rect对象
        self.screen_rect = screen.get_rect() # 屏幕的矩形框

        self.rect.centerx = self.screen_rect.centerx # 将飞船矩形的x轴中心点与屏幕矩形的X轴中心点重合
        self.rect.bottom = self.screen_rect.bottom # 将飞船矩形的底部与屏幕矩形的底部重合
        # 即飞船在屏幕底部中心

        self.center = float(self.rect.centerx) # 函数float将centerx的值转化为小数

        self.moving_right = False # 向右移动 ,初始值设为False
        self.moving_left = False # 向左移动 ,初始值设为False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: # 如果向右移动，并且飞船矩形的右边缘小于屏幕的右边缘的话
            self.center += self.ai_settings.ship_speed_factor # 飞船向右移动设置的像素单位
        if self.moving_left and self.rect.left > 0: # 向左移动时并且矩形左边缘大于0,及大于屏幕左边缘的话
            self.center -= self.ai_settings.ship_speed_factor # 飞船向左移动设置的像素单位

        self.rect.centerx = self.center # 根据self.center更新rect对象，rect取center的整数部分

    def blitme(self):
        self.screen.blit(self.image, self.rect) # 通过方法blitme()，将飞船图像加载到self.rect指定的位置上

    def center_ship(self):
        self.center = self.screen_rect.centerx # 让飞船在屏幕上居中