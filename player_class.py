"""
File for the player class.
"""

import pygame
from bird_class import BirdCharacter

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BASE_PLAYER_HP = 500
BASE_PLAYER_ATK = 10
BASE_PLAYER_SPD = 5
SPRITE_WIDTH = 100
SPRITE_HEIGHT = 100

PLAYER_START_LOCATION = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - SPRITE_HEIGHT)


class Player(BirdCharacter):
    def __init__(self, sprite_path):

        # stats
        self._max_hp = BASE_PLAYER_HP
        self._remaining_hp = BASE_PLAYER_HP
        self._atk = BASE_PLAYER_ATK
        self._is_dead = False
        self._player_heading = 0

        # Set up sprite and rectangles
        self._sprite_path = sprite_path
        self._sprite_img = pygame.image.load(self._sprite_path).convert_alpha()
        self._sprite_img = pygame.transform.scale(
            self._sprite_img, (SPRITE_WIDTH, SPRITE_HEIGHT)
        )
        self._sprite_rect = self._sprite_img.get_rect(center=PLAYER_START_LOCATION)

    def draw(self, screen):

        # Draw player on the screen
        screen.blit(self._sprite_img, self._sprite_rect)

        # Draw HP bar a bit above enemy location
        percent_hp_remain_bar = (
            self._remaining_hp / self._max_hp
        ) * self._sprite_rect.width
        pygame.draw.rect(
            screen,
            "Red",
            pygame.Rect(
                self.sprite_rect.x, self.sprite_rect.y - 10, percent_hp_remain_bar, 7
            ),
        )

    def _die(self):
        """
        Makes player disappear from the screen when their remaining HP reaches
        0.
        """
        if self._remaining_hp <= 0:
            self._is_dead = True

    def move(self):
        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self._sprite_rect.x -= 5
        if keys[pygame.K_d]:
            self._sprite_rect.x += 5
        if keys[pygame.K_w]:
            self._sprite_rect.y -= 5
        if keys[pygame.K_s]:
            self._sprite_rect.y += 5

        # player rotation
        if keys[pygame.K_UP]:
            if self._player_heading == 0:
                change = 90
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 180:
                change = -90
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 270:
                change = -180
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
        if keys[pygame.K_DOWN]:
            if self._player_heading == 0:
                change = 270
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 90:
                change = 180
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 180:
                change = 90
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
        if keys[pygame.K_LEFT]:
            if self._player_heading == 0:
                change = 180
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 90:
                change = 90
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 270:
                change = -90
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
        if keys[pygame.K_RIGHT]:
            if self._player_heading == 90:
                change = -90
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 180:
                change = -180
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
            elif self._player_heading == 270:
                change = -270
                self._sprite_img = pygame.transform.rotate(self._sprite_img, change)
                self._player_heading += change
