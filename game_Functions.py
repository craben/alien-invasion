# -*- coding:utf-8 -*-
# Author:gaoy
# Time  :2020/3/2  下午 3:02

import sys
import pygame
from bullet import Bullet
from alien import Alien
import random
from time import sleep


#  更新屏幕上的图像，并切换到新屏幕
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)
    # 显示得分
    sb.show_score()
    ship.blitme()
    aliens.draw(screen)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


# 响应按键按下
def check_keydown_events(ai_settings, screen, stats, sb, event, ship, aliens, bullets):
    # 定义飞机的上下左右移动
    if event.key in (pygame.K_RIGHT, pygame.K_d):
        ship.moving_right = True
    elif event.key in (pygame.K_LEFT, pygame.K_a):
        ship.moving_left = True
    elif event.key in (pygame.K_UP, pygame.K_w):
        ship.moving_up = True
    elif event.key in (pygame.K_DOWN, pygame.K_s):
        ship.moving_down = True
    # 用空格开火
    elif event.key in (pygame.K_SPACE, pygame.K_KP_ENTER):
        fire_bullet(ai_settings, screen, ship, bullets)
    # 用键盘ESC退出游戏
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif (event.key == pygame.K_p) and not stats.game_active:  # 检测是否按下P键，如果是重新开始游戏
        start_game(ai_settings, screen, stats, sb, aliens, bullets, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# 响应按键松开
def check_keyup_events(event, ship):
    if event.key in (pygame.K_RIGHT, pygame.K_d):
        ship.moving_right = False
        # print('ship right moving')
    elif event.key in (pygame.K_LEFT, pygame.K_a):
        ship.moving_left = False
        # print('ship left moving')
    elif event.key in (pygame.K_UP, pygame.K_w):
        ship.moving_up = False
        # print('ship up moving')
    elif event.key in (pygame.K_DOWN, pygame.K_d):
        ship.moving_down = False
        # print('ship down moving')


# 更新子弹位置并删除已消失的子弹
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中外星人
    # 如果是这样，就删除相应的子弹和外星人
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


# 检测飞船发射的子弹是否与外星人碰撞
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
            check_high_score(stats, sb)
    # 检查外星人组中是否还有外星人，如果没有则清除子弹，创建新的外星人
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, screen, stats, sb, event, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        # 检测鼠标按下
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


# 在玩家点击开始按钮后开始游戏
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, aliens, bullets, ship)


# 重新开始游戏初始化游戏状态
def start_game(ai_settings, screen, stats, sb, aliens, bullets, ship):
    # 影藏光标
    pygame.mouse.set_visible(False)
    # 设置恢复默认值
    ai_settings.initialize_dynamic_settings()
    stats.reset_stats()
    stats.game_active = True
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_ships()

    # 创建一群新的外星人，并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


# 创建外星人编组
def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_aliens_y = get_number_aliens_y(ai_settings, alien.rect.height, ship.rect.height)
    for row_number in range(number_aliens_y):
        for column_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, row_number, column_number)


# 计算每行可容纳多少外星人
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return random.randint(0, number_aliens_x)


# 计算每列可以容纳多少外星人
def get_number_aliens_y(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return random.randint(0, number_aliens_y)


# 在屏幕中创建外星人
def create_alien(ai_settings, screen, aliens, number_aliens_y, number_aliens_x):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * number_aliens_x
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_aliens_y
    aliens.add(alien)


# 更新外星人群中所有外星人的位置
def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人是否达到屏幕底端，如果到达则ship_hit
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)


# 响应被外星人撞到飞船
def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    if stats.ships_life > 0:
        # 将stats.ships_life -1
        stats.ships_life -= 1
        # 将记分牌更新
        sb.prep_ships()
        # 清空子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


# 检测外星人是否到达屏幕边缘
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


# 将整群外星人下移，并改变他们的方向
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


# 检查是否有外星人到达屏幕底端
def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
