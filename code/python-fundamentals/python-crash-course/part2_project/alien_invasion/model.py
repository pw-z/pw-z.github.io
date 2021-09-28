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
        self.bg_color = (255, 255, 255)

        # ship settings
        self.ship_speed_x = 2
        self.ship_speed_y = 1

        # bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 30

        # alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1


class Ship:
    def __init__(self, settings, screen):
        self.screen = screen
        self.setting = settings

        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = float(self.screen_rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.setting.ship_speed_x
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.setting.ship_speed_x
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.setting.ship_speed_y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.setting.ship_speed_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


from pygame.sprite import Sprite
class Bullet(Sprite):
    """
    继承了Sprite类的子弹类
    Sprite类可以将相关元素编组，便于后续统一处理
    """
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.top

        self.y = float(self.rect.centery)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien(Sprite):
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('img/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True