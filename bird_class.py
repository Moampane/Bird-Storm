"""
File for the overarching BirdCharacter class.
"""
from abc import ABC, abstractmethod
import pygame


class BirdCharacter(ABC):
    """
    Abstract base class representing any bird character.

    Attributes:
        _remaining_hp: an integer representing health points left
        _max_hp: an integer representing the max health points
        _atk: an integer representing the ATK stat-- how much damage a
        character does per hit
        _sprite_path: a string representing the file path to the folder
        containing the character's different sprites
        _sprite_img: a pygame surface containing the image of the character
        _sprite_rect: a pygame rectangle mapped to the character sprite
        _is_dead: a boolean telling if the character is dead or not
    """

    @abstractmethod
    def __init__(self, sprite_path):
        """
        Base initialization function for all BirdCharacter subclass instances.
        Will be implemented for each subclass.

        Args:
            sprite_path: a string representing the file path to the character
            sprite images
        """

    @property
    def max_hp(self):
        """
        Returns the maximum health points of a character.
        """
        return self._max_hp

    @property
    def remaining_hp(self):
        """
        Returns the remaining health points of a character.
        """
        return self._remaining_hp

    @property
    def atk(self):
        """
        Returns the atk stat of a character.
        """
        return self._atk

    @property
    def sprite_img(self):
        """
        Returns the pygame image of a character.
        """
        return self._sprite_img

    @property
    def sprite_rect(self):
        """
        Returns the pygame rectangle of a character.
        """
        return self._sprite_rect

    def attack(self, target):
        """
        Carries out attack animation and damage done to a target.

        Args:
            target: a BirdCharacter class (either enemy or player)
        """
        # -- attack animation -- #
        if self._sprite_rect.colliderect(target.sprite_rect):
            target.take_damage(self._atk)

    def take_damage(self, opponent_atk):
        """
        Lose an amount of HP based on opponent's ATK stat.

        Args:
            opponent_atk: an integer representing the opponent's atk stat
        """
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self._die()

    @abstractmethod
    def draw(self, screen):
        """
        Base function for drawing the character and associated information on
        the screen. Will be implemented in subclasses.

        Args:
            screen: the pygame display surface
        """

    @abstractmethod
    def _die(self):
        """
        Base function for when a character reaches 0HP. Will be implemented in
        subclasses.
        """
