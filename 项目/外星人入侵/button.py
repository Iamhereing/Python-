import pygame.font # 模块pygame.font能够将文本渲染到屏幕上

class Button():

    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50 # 按钮的宽高
        self.button_color = (0, 255, 0) # 按钮的背景颜色
        self.text_color = (255, 255, 255) # 按钮的文本颜色
        self.font = pygame.font.SysFont(None, 48) # 指定文本的字体和字号

        self.rect = pygame.Rect(0,0, self.width, self.height) # 将按钮加载在屏幕0,0处
        self.rect.center = self.screen_rect.center # 将按钮的center属性设置为屏幕的center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # font.render()将存储在msg中的文本转换为图像，然后存储在msg-image中。
        # True是指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑），另外
        # 两个指定文本颜色和按钮颜色
        self.msg_image_rect = self.msg_image.get_rect() #根据文本图像创建一个rect
        self.msg_image_rect.center = self.rect.center # 将其center属性设置为按钮的center属性
        # 即文本图像在按钮上居中

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect) # screen.fill（）来绘制表示按钮的矩形，并填充颜色
        self.screen.blit(self.msg_image, self.msg_image_rect) # screen.blit()传递文本图像及其矩形