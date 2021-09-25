#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from model import Setting
from model import Ship
import function as func


def run_game():
    st = Setting()

    pygame.init()
    screen = pygame.display.set_mode((st.screen_width, st.screen_height))
    pygame.display.set_caption(st.game_caption)

    ship = Ship(st, screen)

    while True:
        func.check_events(ship)
        ship.update()
        func.update_screen(st, screen, ship)


if __name__ == '__main__':
    run_game()
