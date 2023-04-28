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
    def __init__(self, image_path, screen):
        super().__init__(image_path, screen)
        self.max_hp = MAX_PLAYER_HEALTH
        self.remaining_hp = self.max_hp
        self.atk = PLAYER_ATK
        self.ms = PLAYER_MOVESPEED
        self.image = pygame.image.load(image_path).convert_alpha()
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.start_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
        self.rect = self.image.get_rect(center=self.start_pos)
        self.isdead = False
        self.screen = screen
        self._is_facing_right = True
        self._is_facing_forward = True
        self._is_atking = False
        self._char_name = image_path.partition("_")[0]
        self._player_heading = 0

    def update_img(self):
        """
        Updates the character image to be correct according to the current
        attack and heading position.
        """
        if self._is_facing_forward:
            front_or_back = "front"
        else:
            front_or_back = "back"

        if self._is_facing_right:
            left_or_right = "right"
        else:
            left_or_right = "left"

        if self._is_atking:
            atk_or_idle = "atk"
        else:
            atk_or_idle = "idle"

        updated_img_path = (
            f"{self._char_name}_{front_or_back}_{left_or_right}_{atk_or_idle}.png"
        )

        self.image = pygame.image.load(updated_img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        # player movement
        if keys[pygame.K_a]:
            self.rect.x -= self.ms
            self._is_facing_right = False
            self._player_heading = 180
        if keys[pygame.K_d]:
            self.rect.x += self.ms
            self._is_facing_right = True
            self._player_heading = 0
        if keys[pygame.K_w]:
            self.rect.y -= self.ms
            self._is_facing_forward = False
            self._player_heading = 90
        if keys[pygame.K_s]:
            self.rect.y += self.ms
            self._is_facing_forward = True
            self._player_heading = 270

        self.update_img()

        # # player rotation
        # if keys[pygame.K_UP]:
        #     if self._player_heading == 0:
        #         change = 90
        #         self._image = pygame.transform.rotate(self._image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 180:
        #         change = -90
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 270:
        #         change = -180
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        # if keys[pygame.K_DOWN]:
        #     if self._player_heading == 0:
        #         change = 270
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 90:
        #         change = 180
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 180:
        #         change = 90
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        # if keys[pygame.K_LEFT]:
        #     if self._player_heading == 0:
        #         change = 180
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 90:
        #         change = 90
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 270:
        #         change = -90
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        # if keys[pygame.K_RIGHT]:
        #     if self._player_heading == 90:
        #         change = -90
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 180:
        #         change = -180
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change
        #     elif self._player_heading == 270:
        #         change = -270
        #         self.image = pygame.transform.rotate(self.image, change)
        #         self._player_heading += change


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
