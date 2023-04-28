"""
File for overarching bird classes.
"""
import pygame


class BirdCharacter(pygame.sprite.Sprite):
    def __init__(self, image_path, screen):
        pygame.sprite.Sprite.__init__(self)
        self._image = pygame.image.load(image_path)
        self._isdead = False
        self._screen = screen

    def take_damage(self, opponent_atk):
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()

    def update(self):
        # Health bar
        hp_bar_percent = self._remaining_hp / self._max_hp * self._width
        pygame.draw.rect(
            self._screen,
            "Green",
            pygame.Rect(self.rect.x, self.rect.y - 10, hp_bar_percent, 7),
        )
