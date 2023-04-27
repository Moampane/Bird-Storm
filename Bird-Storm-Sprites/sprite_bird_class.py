"""
File for overarching bird classes.
"""
import pygame


class BirdCharacter(pygame.sprite.Sprite):
    def __init__(self, max_health, attack, movespeed, image_path, start_pos, size, bg):
        pygame.sprite.Sprite.__init__(self)
        self.max_hp = max_health
        self.remaining_hp = self.max_hp
        self.atk = attack
        self.ms = movespeed
        self.image = pygame.image.load(image_path)
        self.width = size[0]
        self.height = size[1]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=start_pos)
        self.isdead = False
        self.screen = bg

    def take_damage(self, opponent_atk):
        self.remaining_hp -= opponent_atk
        if self.remaining_hp <= 0:
            self.kill()

    def update(self):
        # Health bar
        hp_bar_percent = self.remaining_hp / self.max_hp * self.width
        pygame.draw.rect(
            self.screen,
            "Green",
            pygame.Rect(self.rect.x, self.rect.y - 10, hp_bar_percent, 7),
        )
