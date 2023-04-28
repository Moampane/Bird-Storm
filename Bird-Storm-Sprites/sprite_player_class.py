"""
File for player classes.
"""
import pygame, sprite_bird_class


class Player(sprite_bird_class.BirdCharacter):
    def __init__(self, max_health, attack, movespeed, image_path, start_pos, size, bg):
        super().__init__(max_health, attack, movespeed, image_path, start_pos, size, bg)
        self._player_heading = 0

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        # player movement
        if keys[pygame.K_a]:
            self.rect.x -= self.ms
        if keys[pygame.K_d]:
            self.rect.x += self.ms
        if keys[pygame.K_w]:
            self.rect.y -= self.ms
        if keys[pygame.K_s]:
            self.rect.y += self.ms

        # player rotation
        if keys[pygame.K_UP]:
            if self._player_heading == 0:
                change = 90
                self.image = pygame.transform.rotate(self.image, change)
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
