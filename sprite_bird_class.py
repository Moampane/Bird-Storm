"""
File for overarching bird classes.
"""
import pygame


class BirdCharacter(pygame.sprite.Sprite):
    def __init__(self, image_path, screen):
        pygame.sprite.Sprite.__init__(self)
        self._image = pygame.image.load(image_path).convert_alpha()
        self._isdead = False
        self._screen = screen

    @property
    def image(self):
        """
        Returns the character's pygame image.
        """
        return self._image

    @property
    def rect(self):
        """
        Returns the character's pygame rectangle.
        """
        return self._rect

    @property
    def atk(self):
        """
        Returns the character's integer attack stat.
        """
        return self._atk

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
            pygame.Rect(self._rect.x, self._rect.y - 10, hp_bar_percent, 7),
        )
