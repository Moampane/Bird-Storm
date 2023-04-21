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
        _sprite_img = a pygame surface containing the image of the character
        _sprite_rect = a pygame rectangle mapped to the character sprite
    """

    def __init__(self, sprite_path):
        # Set stats to 0 for now
        self._max_hp = 0
        self._remaining_hp = 0
        self._atk = 0

        # load character imgs in pygame
        self._sprite_path = sprite_path
        self._sprite_img = pygame.image.load(sprite_path).convert_alpha()
        self._sprite_rect = self._sprite_img.get_rect()

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
        # logic for if target is within the hitbox
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
    def _die(self):
        """
        Base function for when a character reaches 0HP. Will be implemented in
        subclasses.
        """
