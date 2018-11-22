import pygame
from pygame.sprite import Sprite # 通过Sprite类，可将游戏中相关
                                    # 的元素编组，进而同时操作编组中的所有元素

class Bullet(Sprite): # 定义关于子弹的类

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen # 初始化屏幕

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height) # 先在（0,0）处设置一
                                        # 个表示子弹的矩形，载入子弹的宽高初始值
        self.rect.centerx = ship.rect.centerx # 将子弹的中心位置对准飞船的中心位置
        self.rect.top = ship.rect.top # 将子弹的顶部对准飞船的顶部
        self.y = float(self.rect.y) # 将子弹的Y坐标设置成小数值，以便
                                                                             # 可以微调子弹的速度

        self.color = ai_settings.bullet_color # 子弹的颜色就是初始设置的颜色
        self.speed_factor = ai_settings.bullet_speed_factor # 子弹的速度就是初始设置的速度

    def update(self): # 定义向上移动子弹

        self.y -= self.speed_factor # 子弹的初始位置减去移动的速度单位，及代表有小数值的子弹位置
        self.rect.y = self.y # 子弹的位置即子弹矩形的位置

    def draw_bullet(self): # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect) # 表示在屏幕上显示有颜色的子弹矩形块