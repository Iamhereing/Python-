import sys, pygame

from settings import Settings

from dog import Dog

def run_game():
    # 先初始化游戏
    pygame.init()
    # 初始化游戏的设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 为这个游戏取一个标题
    pygame.display.set_caption("Dog Home")

    # 创建一只狗狗
    dog = Dog(screen)

    #  开始游戏的循环
    while True:
        # 当事件类型是退出游戏时，即结束游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每一次事件结束后，都重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        dog.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

# 运行游戏
run_game()