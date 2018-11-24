import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets): # 定义按键的函数
    if event.key == pygame.K_LEFT:  # 当按左键时
        ship.moving_left = True  # 将初始状态False转为True，坐标向左移动一个单位
    if event.key == pygame.K_RIGHT:  # 当按右键时
        ship.moving_right = True  # 将初始状态False转为True，坐标向右移动一个单位

    elif event.key == pygame.K_SPACE: # 当按空格键时
        fire_bullet(ai_settings, screen, ship, bullets) # 开火，即发射子弹

    elif event.key == pygame.K_q: # 当按下q键时
        sys.exit() # 退出游戏

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

def update_screen(ai_settings, screen, ship, aliens, bullets): # 刷新屏幕的函数
    screen.fill(ai_settings.bg_color)  # 每次循环时都重绘屏幕,即矢量图形的背景颜色
    for bullet in bullets.sprites(): # 发射子弹组的每一个子弹
        bullet.draw_bullet() # 绘制子弹
    ship.blitme()  # 将飞船加载在屏幕，确保出现在背景前面
    aliens.draw(screen) # 将外星人加载在屏幕

    pygame.display.flip()  # 命令Pygame让最近绘制的屏幕可见。
    # 在这里，它在每次执行while循环时都绘制一个空屏幕，并擦
    # 去旧屏幕，使得只有新屏幕可见。在我们移动游戏元素时，
    # pygame.display.flip（）将不断更新屏幕，以显示元素的的新
    # 位置，并在原来的位置隐藏元素，从而营造平滑移动的效果

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():  # 方法copy()是设置for循环的，从而能够在循环中修改bullets
        if bullet.rect.bottom <= 0:  # 如果子弹矩形的地步小于等于0,即子弹顶部离开屏幕顶部
            bullets.remove(bullet)  # 从子弹组中删除这颗子弹
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 方法sprite.groupcollide()将子弹矩形与外星人矩形进行比较，
    # 并返回一个字典。字典K：子弹 V：被击中的外星人，两个True
    # 代表删除发生碰撞的子弹和外星人

    if len(aliens) == 0: # 如果外星人被打完了
        bullets.empty() # 删除所有的子弹
        create_fleet(ai_settings, screen, ship, aliens) # 再添加一群外星人

def get_number_aliens_x(ai_settings, alien_width): # 计算可容纳外星人的个数
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 可允许
    # 外星人的个数的宽度=屏幕宽度-2×外星人宽度（边距为一个外星人的宽度）
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 外星人的个数=
    # 可允许外星人个数/2外星人宽度（外星人之间的间距为一个外星人宽度）
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height): # 计算屏幕可容纳多少行外星人
    available_space_y = (ai_settings.screen_height - (3 * alien_height)
                         -ship_height) # 可容纳的空间高度=屏幕的高度-上边距
                                                      # -第一行外星人高度及间距-飞船高度
    number_rows = int(available_space_y / (2 * alien_height)) # 外星人行数
                                               # = 可容纳的空间高度 / 外星人高度及行距
    return number_rows # 返回可容纳外星人的行数

def create_alien(ai_settings, screen, aliens, alien_number, row_number): # 定义一行外星人
    alien = Alien(ai_settings, screen)  # 导入设置好的外星人的类
    alien_width = alien.rect.width  # 外星人的宽度等于外星人图片矩形的宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x  # 一行外星人的X值=
    # 左边边距+（一个外星人+其间距）×外星人个数
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # 一列外星人的Y值=第一行外星人的高度+剩下外星人的高度及间距×一列的个数
    aliens.add(alien)  # 将每个新创建的外星人都添加到编组aliens中

def create_fleet(ai_settings, screen, ship, aliens): # 创建外星人群
    alien = Alien(ai_settings, screen) # 导入设置好的外星人的类
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):  # 循环每一个外星人，即加载第一行外星人
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens): # 检查到当有外星人到达边缘时
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break # 到达边缘时退出循环

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed # 外星人向下移动初始设置单位
    ai_settings.fleet_direction *= -1 # 向左移动

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets): # 定义被撞到的飞船
    if stats.ships_left > 0:
        stats.ships_left -= 1  # 当被撞时储存的飞船数量减1

        aliens.empty()  # 外星人清空
        bullets.empty()  # 子弹清空

        create_fleet(ai_settings, screen, ship, aliens)  # 新添加一群外星人群
        ship.center_ship()  # 将飞船放在屏幕底端中央

        sleep(0.5)  # 暂停

    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # 定义外星人触碰到屏幕底部的函数
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets): # 更新外星人群的类
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # 方法spritecollideany（）接受两个实参：一个精灵和一个编组。
    # 它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生
    # 了碰撞后的成员后就停止遍历编组。在此处，它遍历编组aliens，
    # 并返回它找到的的第一个与飞船发生碰撞的外星人。如果发生
    # 碰撞，执行ship_hit的操作
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)





