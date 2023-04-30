"""
File containing the class for an attack.
"""
import pygame

pygame.init()
ATK_FONT = pygame.font.SysFont("arial", 30, bold=True)


class Attack(pygame.sprite.Sprite):
    """
    Class representing a character's attack.

    Attributes:
        _character: A BirdCharacter instance representing the attacking
        character.
        _image: A pygame image representing the character's attack hitbox.
        _rect: A pygame rectangle mapped to the attack's image
        _animation_loop: An int representing the frame the animation is on.
    """

    def __init__(self, character, group):
        """
        Constructor for Attack class.

        Args:
            character: A BirdCharacter instance representing the attacking
            character.
            group: A pygame sprite group holding the Attack object.
        """
        super().__init__()
        group.add(self)
        self._character = character
        self._image = ATK_FONT.render("BONK", False, "Red")
        self._rect = self._image.get_rect(center=(-1000, -1000))
        self._animation_loop = 0

    def update(self):
        """
        Updates status of the attack.
        """
        big_gap = 150
        small_gap = 50
        if self._character.heading == 0:
            self._rect = self._image.get_rect(
                center=(
                    self._character.rect.x + big_gap,
                    self._character.rect.y + small_gap,
                )
            )
        if self._character.heading == 90:
            self._rect = self._image.get_rect(
                center=(
                    self._character.rect.x + small_gap,
                    self._character.rect.y - small_gap,
                )
            )
        if self._character.heading == 180:
            self._rect = self._image.get_rect(
                center=(
                    self._character.rect.x - small_gap,
                    self._character.rect.y + small_gap,
                )
            )
        if self._character.heading == 270:
            self._rect = self._image.get_rect(
                center=(
                    self._character.rect.x + small_gap,
                    self._character.rect.y + big_gap,
                )
            )
        self._animation_loop += 0.5
        if self._animation_loop >= 5:
            self.kill()

    @property
    def image(self):
        """
        Returns the pygame image of the attack.
        """
        return self._image

    @property
    def rect(self):
        """
        Returns the pygame rectangle of the attack.
        """
        return self._rect
