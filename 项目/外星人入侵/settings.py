class Settings(): # 存储该游戏所有设置的类

    def __init__(self):
        self.screen_width = 1200 # 自定义屏幕的宽
        self.screen_height = 800 # 自定义屏幕的高
        self.bg_color = (230, 230, 230) # 自定义屏幕的背景色

        self.ship_speed_factor = 1.5 # 飞船移动的像素的初始值

        self.bullet_speed_factor = 1 # 子弹速度的初始值
        self.bullet_width = 3 # 子弹的宽度
        self.bullet_height = 15 # 子弹的高度
        self.bullet_color = 60, 60, 60 # 子弹的颜色
        self.bullets_allowed = 3 # 设置子弹的个数为3个
