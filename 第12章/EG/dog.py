import pygame

class Dog():
    def __init__(self,screen):
        # 初始化狗狗并设置狗狗的初始化位置
        self.screen = screen

        # 加载狗狗图像并获取外接矩形
        self.image = pygame.image.load('images/dog.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每只狗狗放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # 在指定位置绘制狗狗
        self.screen.blit(self.image, self.rect)