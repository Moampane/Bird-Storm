"""
File for player classes.
"""
import pygame
from sprite_bird_class import BirdCharacter

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

MAX_PLAYER_HEALTH = 1000
PLAYER_ATK = 5
PLAYER_MOVESPEED = 5
PLAYER_START_POS = SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100


class Player(BirdCharacter):
    def __init__(self, image_path, bg):
        super().__init__(image_path, bg)
        self._max_hp = MAX_PLAYER_HEALTH
        self._remaining_hp = self._max_hp
        self._atk = PLAYER_ATK
        self._ms = PLAYER_MOVESPEED
        self._image = pygame.image.load(image_path).convert_alpha()
        self._width = PLAYER_WIDTH
        self._height = PLAYER_HEIGHT
        self._image = pygame.transform.scale(self._image, (self._width, self._height))
        self._start_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
        self._rect = self.image.get_rect(center=self._start_pos)
        self._isdead = False
        self._screen = bg
        self._is_facing_right = True
        self._is_facing_forward = True
        self._is_atking = False

    def update_img(self):
        """
        Updates the character image to be correct according to the current
        attack and heading position.
        """
        self._image = pygame.image.load(image_path).convert_alpha()
        self._image = pygame.transform.scale(self._image, (self._width, self._height))
    
    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        # player movement
        if keys[pygame.K_a]:
            self._rect.x -= self._ms
            
        if keys[pygame.K_d]:
            self._rect.x += self._ms
        if keys[pygame.K_w]:
            self._rect.y -= self._ms
        if keys[pygame.K_s]:
            self._rect.y += self._ms

        # player rotation
        if keys[pygame.K_UP]:
            if self._player_heading == 0:
                change = 90
                self._image = pygame.transform.rotate(self._image, change)
                self._player_heading += change
            elif self._player_heading == 180:
                change = -90
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
            elif self._player_heading == 270:
                change = -180
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
        if keys[pygame.K_DOWN]:
            if self._player_heading == 0:
                change = 270
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
            elif self._player_heading == 90:
                change = 180
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
            elif self._player_heading == 180:
                change = 90
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
        if keys[pygame.K_LEFT]:
            if self._player_heading == 0:
                change = 180
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
            elif self._player_heading == 90:
                change = 90
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
            elif self._player_heading == 270:
                change = -90
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
        if keys[pygame.K_RIGHT]:
            if self._player_heading == 90:
                change = -90
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
            elif self._player_heading == 180:
                change = -180
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change
            elif self._player_heading == 270:
                change = -270
                self.image = pygame.transform.rotate(self.image, change)
                self._player_heading += change

    def attack()


class Attack(pygame.sprite.Sprite):
    def __init__(self, character, group):
        super().__init__()
        group.add(self)
        self.player = character
        self.image = pygame.image.load("graphics/bite.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(-1000, -1000))
        self.animation_loop = 0

        # self.animation_loop = 0
        # self.group = attack_group
        # center=(self.player.rect.x, self.player.rect.y)

    def update(self):
        if self.player._player_heading == 0:
            self.rect = self.image.get_rect(
                center=(self.player.rect.x + 150, self.player.rect.y + 50)
            )
        if self.player._player_heading == 90:
            self.rect = self.image.get_rect(
                center=(self.player.rect.x + 50, self.player.rect.y - 50)
            )
        if self.player._player_heading == 180:
            self.rect = self.image.get_rect(
                center=(self.player.rect.x - 50, self.player.rect.y + 50)
            )
        if self.player._player_heading == 270:
            self.rect = self.image.get_rect(
                center=(self.player.rect.x + 50, self.player.rect.y + 150)
            )
        self.animation_loop += 0.5
        if self.animation_loop >= 5:
            self.kill()
