"""
File containing the class for an attack.
"""
import pygame

pygame.init()
ATK_FONT = pygame.font.SysFont("arial", 30, bold=True)


class Attack(pygame.sprite.Sprite):
    """
    Class representing the player's attack.

    Attributes:
        _player: A Player object representing the player's character.
        _image: A pygame image representing the player's attack animation.
        _rect: A pygame rectangle mapped to the attack's image
        _animation_loop: An int representing the frame the animation is on.
    """

    def __init__(self, character, group):
        """
        Constructor for Attack class.

        Args:
            character: A Player object representing the player's character.
            Assigned to _player attribute.
            group: A pygame sprite group holding the Attack object.
        """
        super().__init__()
        group.add(self)
        self._player = character
        self._image = ATK_FONT.render("BONK", False, "Red")
        # self._image = pygame.transform.scale(self._image, (100, 100))
        self._rect = self._image.get_rect(center=(-1000, -1000))
        self._animation_loop = 0

    def update(self):
        big_gap = 150
        small_gap = 50
        if self._player.heading == 0:
            self._rect = self._image.get_rect(
                center=(
                    self._player.rect.x + big_gap,
                    self._player.rect.y + small_gap,
                )
            )
        if self._player.heading == 90:
            self._rect = self._image.get_rect(
                center=(
                    self._player.rect.x + small_gap,
                    self._player.rect.y - small_gap,
                )
            )
        if self._player.heading == 180:
            self._rect = self._image.get_rect(
                center=(
                    self._player.rect.x - small_gap,
                    self._player.rect.y + small_gap,
                )
            )
        if self._player.heading == 270:
            self._rect = self._image.get_rect(
                center=(
                    self._player.rect.x + small_gap,
                    self._player.rect.y + big_gap,
                )
            )
        self._animation_loop += 0.5
        if self._animation_loop >= 5:
            self.kill()

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect
