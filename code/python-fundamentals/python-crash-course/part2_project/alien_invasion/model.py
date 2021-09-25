import pygame.image


class Setting:
    """all settings of the game"""

    def __init__(self):
        """init the game setting"""
        # game info
        self.game_caption = 'Alien Invasion'

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 10)

        # ship settings
        self.ship_speed = 2


class Ship:
    def __init__(self, settings, screen):
        self.screen = screen
        self.setting = settings

        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.setting.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.setting.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.setting.ship_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
