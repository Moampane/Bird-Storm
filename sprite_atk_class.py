"""
File containing the class for an attack.
"""
import pygame

pygame.init()
ATK_FONT = pygame.font.Font("fonts/pixel.ttf", 40)


class Attack(pygame.sprite.Sprite):
    """
    Class representing a character's attack.

    Attributes:
        _character: A BirdCharacter instance representing the attacking
        character.
        _image: A pygame image representing the character's attack hitbox.
        _rect: A pygame rectangle mapped to the attack's image.
        _animation_loop: An int representing the frame the animation is on.
        _first_hit: A boolean representing whether the first hit has
        occurred or not.
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
        self._first_hit = True

    def update(self):
        """
        Updates status of the attack.
        """
        # big_gap = 150
        # small_gap = 50
        # if self._character.heading == 0:
        #     self._rect = self._image.get_rect(
        #         center=(
        #             self._character.rect.x + big_gap,
        #             self._character.rect.y + small_gap,
        #         )
        #     )
        # if self._character.heading == 90:
        #     self._rect = self._image.get_rect(
        #         center=(
        #             self._character.rect.x + small_gap,
        #             self._character.rect.y - small_gap,
        #         )
        #     )
        # if self._character.heading == 180:
        #     self._rect = self._image.get_rect(
        #         center=(
        #             self._character.rect.x - small_gap,
        #             self._character.rect.y + small_gap,
        #         )
        #     )
        # if self._character.heading == 270:
        #     self._rect = self._image.get_rect(
        #         center=(
        #             self._character.rect.x + small_gap,
        #             self._character.rect.y + big_gap,
        #         )
        #     )

        # different way of attacking, test if this is better?
        if self._character.is_facing_right():
            self._rect = self._image.get_rect(
                topleft=(self._character.rect.topright)
            )
        else:
            self._rect = self._image.get_rect(
                topright=self._character.rect.topleft
            )

        self._animation_loop += 0.5
        self._character.set_atk_status(True)
        if self._animation_loop >= 5:
            self._character.set_atk_status(False)
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

    @property
    def first_hit(self):
        """
        Returns bool saying whether it's the first hit of the attack or not.
        """
        return self._first_hit

    def set_first_hit_false(self):
        """
        Sets status of _first_hit to false after the attack has hit the target
        once.
        """
        self._first_hit = False
