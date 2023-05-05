"""
File containing the class for an attack.
"""
import pygame

pygame.init()
ATK_FONT = pygame.font.Font("fonts/pixel.ttf", 40)
ATK_SCALE = 2
MAX_ANIMATION_TIME = 5
ANIMATION_LOOP_INCREMENT = 0.5


class Attack(pygame.sprite.Sprite):
    """
    Class representing a character's attack.

    Attributes:
        _character: A BirdCharacter instance representing the attacking
        character.
        _image: A pygame image representing the character's attack hitbox.
        _rect: A pygame rectangle mapped to the attack's image.
        occurred or not.
        _txt_width: An int representing the width of the textbox of the attack.
        _txt_height: An int representing the height of the textbox of the
        attack.
        _animation_loop: An int representing the frame the animation is on.
        _first_hit: A boolean representing whether the first hit has.
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
        self._txt_width = self._rect.width
        self._txt_height = self._rect.height
        self._animation_loop = 0
        self._first_hit = True

    def update(self):
        """
        Updates status of the attack.
        """
        if self._character.is_facing_right():
            self._rect = self._image.get_rect(
                center=(
                    self._character.rect.topright[0] + self._txt_width / 2,
                    self._character.rect.topright[1] + self._txt_height / 2,
                )
            )
            self._rect.width = self._rect.width * ATK_SCALE
            self._rect.height = self._rect.height * ATK_SCALE
        else:
            self._rect = self._image.get_rect(
                center=(
                    self._character.rect.topleft[0] - self._txt_width / 2,
                    self._character.rect.topleft[1] + self._txt_height / 2,
                )
            )
            self._rect.width = self._rect.width * ATK_SCALE
            self._rect.height = self._rect.height * (ATK_SCALE + 1)

        self._animation_loop += ANIMATION_LOOP_INCREMENT
        self._character.set_atk_status(True)
        if self._animation_loop >= MAX_ANIMATION_TIME:
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
        Returns the pygame rectangle outlining the attack.
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
