#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from model import Setting,Ship, Alien
import function as func
from pygame.sprite import Group


def run_game():
    st = Setting()

    pygame.init()
    screen = pygame.display.set_mode((st.screen_width, st.screen_height))
    pygame.display.set_caption(st.game_caption)

    ship = Ship(st, screen)
    # alien = Alien(st, screen)
    bullets = Group()
    aliens = Group()
    func.create_fleet(st, screen, ship, aliens)

    while True:
        func.check_events(st, screen, ship, bullets)
        ship.update()
        func.update_bullets(bullets, aliens)
        func.update_aliens(st, aliens)
        func.update_screen(st, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
