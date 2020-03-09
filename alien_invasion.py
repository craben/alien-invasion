# -*- coding:utf-8 -*-
# Author:gaoy
# Time  :2020/3/2 上午 11:47
import sys
import pygame
from settings import Settings
from ship import Ship
import game_Functions as gf
from pygame.sprite import Group
from game_states import GameStates
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 设置背景色
    ai_settings = Settings()
    # 返回一个surface对象，surface对象是屏幕的一部分，属于显示元素
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    # 实例化存储游戏统计信息的实例
    stats = GameStates(ai_settings)
    # 创建按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    # 创建一个用于存储外星人的编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏循环
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():  # 访问Pygame检测到的事件
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # 检测Pygame的事件
        # screen.fill(ai_settings.bg_color)  # 背景填充
        # ship.blitme()  # 在屏幕中显示飞船
        # # 让最近的屏幕可见
        # pygame.display.flip()  # 让最近绘制的屏幕可见

        if stats.game_active:
            ship.update()  # 更新飞船的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

    # bullets.update()  # 子弹位置更新
    # 删除已消失的子弹
    # for bullet in bullets.copy():
    #     if bullet.rect.bottom <= 0:
    #         bullets.remove(bullet)
    #     # print(len(bullets))


run_game()

