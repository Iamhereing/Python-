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
