"""
File for overarching bird classes.
"""
import pygame


class BirdCharacter(pygame.sprite.Sprite):
    def __init__(self, image_path, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.isdead = False
        self.screen = screen

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
