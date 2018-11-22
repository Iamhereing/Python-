import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets): # 定义按键的函数
    if event.key == pygame.K_LEFT:  # 当按左键时
        ship.moving_left = True  # 将初始状态False转为True，坐标向左移动一个单位
    if event.key == pygame.K_RIGHT:  # 当按右键时
        ship.moving_right = True  # 将初始状态False转为True，坐标向右移动一个单位

    elif event.key == pygame.K_SPACE: # 当按空格键时
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:  # 如果子弹的个数小于允许子弹的个数
        new_bullet = Bullet(ai_settings, screen, ship)  # 初始化新子弹
        bullets.add(new_bullet)  # 子弹组等于新加的每一个子弹

def check_keyup_events(event, ship): # 定义松键的函数
    if event.key == pygame.K_LEFT:  # 当按左键时
        ship.moving_left = False  # 初始状态False,坐标不动
    if event.key == pygame.K_RIGHT:  # 当按右键时
        ship.moving_right = False  # 初始状态False,坐标不动

def check_events(ai_settings, screen, ship, bullets): # 响应事件的函数
    for event in pygame.event.get():  # 事件循环，事件就是用户玩游戏时执行的操作，如按键或移动鼠标
        if event.type == pygame.QUIT:  # 如果事件类型是游戏退出
            sys.exit()  # 调用该模块来退出游戏

        elif event.type == pygame.KEYDOWN: # 当有按键的情况时
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP: # 松开按键的情况
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets): # 刷新屏幕的函数
    screen.fill(ai_settings.bg_color)  # 每次循环时都重绘屏幕,即矢量图形的背景颜色
    for bullet in bullets.sprites(): # 发射子弹组的每一个子弹
        bullet.draw_bullet() # 绘制子弹
    ship.blitme()  # 将飞船加载在屏幕，确保出现在背景前面

    pygame.display.flip()  # 命令Pygame让最近绘制的屏幕可见。
    # 在这里，它在每次执行while循环时都绘制一个空屏幕，并擦
    # 去旧屏幕，使得只有新屏幕可见。在我们移动游戏元素时，
    # pygame.display.flip（）将不断更新屏幕，以显示元素的的新
    # 位置，并在原来的位置隐藏元素，从而营造平滑移动的效果

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():  # 方法copy()是设置for循环的，从而能够在循环中修改bullets
        if bullet.rect.bottom <= 0:  # 如果子弹矩形的地步小于等于0,即子弹顶部离开屏幕顶部
            bullets.remove(bullet)  # 从子弹组中删除这颗子弹


