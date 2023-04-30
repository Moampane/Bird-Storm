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
    def __init__(self, sprite_path, attack_path):

        # stats
        self._max_hp = BASE_PLAYER_HP
        self._remaining_hp = BASE_PLAYER_HP
        self._atk = BASE_PLAYER_ATK
        self._is_dead = False
        self._player_heading = 0
        self._atk_interval_tracker = 0
        self._atk_knockback = 25

        # Set up player sprite and rectangles
        self._sprite_img = pygame.image.load(sprite_path).convert_alpha()
        self._sprite_img = pygame.transform.scale(
            self._sprite_img, (SPRITE_WIDTH, SPRITE_HEIGHT)
        )
        self._sprite_rect = self._sprite_img.get_rect(center=PLAYER_START_LOCATION)

        # Set up attack sprite
        self._attack_img = pygame.image.load(attack_path).convert_alpha()
        self._attack_rect = self._attack_img.get_rect()

    def draw(self, screen):

        # Does not draw player if dead
        if self._is_dead:
            return

        # Draw player on the screen
        screen.blit(self._sprite_img, self._sprite_rect)

        # Draw HP bar a bit above enemy location
        percent_hp_remain_bar = (
            self._remaining_hp / self._max_hp
        ) * self._sprite_rect.width
        pygame.draw.rect(
            screen,
            "Green",
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

    def player_attack(self, screen, target):
        keys = pygame.key.get_pressed()
        # player attack
        if keys[pygame.K_SPACE]:
            if self._player_heading == 0:
                self._attack_img = pygame.transform.scale(self._attack_img, (100, 300))
                self._attack_rect = self._attack_img.get_rect(
                    center=(self._sprite_rect.x + 150, self._sprite_rect.y + 50)
                )

            if self._player_heading == 90:
                self._attack_img = pygame.transform.scale(self._attack_img, (300, 100))
                self._attack_rect = self._attack_img.get_rect(
                    center=(self._sprite_rect.x + 50, self._sprite_rect.y - 50)
                )
            if self._player_heading == 180:
                self._attack_img = pygame.transform.scale(self._attack_img, (100, 300))
                self._attack_rect = self._attack_img.get_rect(
                    center=(self._sprite_rect.x - 50, self._sprite_rect.y + 50)
                )
            if self._player_heading == 270:
                self._attack_img = pygame.transform.scale(self._attack_img, (300, 100))
                self._attack_rect = self._attack_img.get_rect(
                    center=(self._sprite_rect.x + 50, self._sprite_rect.y + 150)
                )
            screen.blit(self._attack_img, self._attack_rect)

        # detect hit
        self._atk_interval_tracker += 1
        if self._atk_interval_tracker % 25 == 0:
            self.attack(target)

        # reset attack hitbox
        self._attack_rect = self._attack_img.get_rect(topleft=(-10000, -10000))

    def attack(self, target):
        player_x = self._sprite_rect.x
        player_y = self._sprite_rect.y
        if self._attack_rect.colliderect(target.sprite_rect):
            target.take_damage(self._atk)
            if target._sprite_rect.x > player_x and target._sprite_rect.y < player_y:
                target._sprite_rect.y -= self._atk_knockback
                target._sprite_rect.x += self._atk_knockback
            elif target._sprite_rect.x < player_x and target._sprite_rect.y < player_y:
                target._sprite_rect.y -= self._atk_knockback
                target._sprite_rect.x -= self._atk_knockback
            elif target._sprite_rect.x > player_x and target._sprite_rect.y > player_y:
                target._sprite_rect.y += self._atk_knockback
                target._sprite_rect.x += self._atk_knockback
            else:
                target._sprite_rect.y += self._atk_knockback
                target._sprite_rect.x -= self._atk_knockback

    def move(self):
        keys = pygame.key.get_pressed()
        # player movement
        if keys[pygame.K_a]:
            self._sprite_rect.x -= BASE_PLAYER_SPD
        if keys[pygame.K_d]:
            self._sprite_rect.x += BASE_PLAYER_SPD
        if keys[pygame.K_w]:
            self._sprite_rect.y -= BASE_PLAYER_SPD
        if keys[pygame.K_s]:
            self._sprite_rect.y += BASE_PLAYER_SPD

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
