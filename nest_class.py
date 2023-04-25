"""
File for the Nest Interactable class
"""
import pygame
import random
from interactable_class import Interactable


class Nest(Interactable):
    """
    Class representing the interactable object Nest to raise Player stats.

    Attributes:

        _target_stat: a string representing the target stat of the player that
        the interactable increases
        _percent_increased: an integer representing the increased amount of a
        specific stat in the player
    """

    def __init__(self, img_path):
        super().__init__(img_path)
        self._target_stat = random.choice(["ATK", "HP"])
        self._percent_increased = random.randint(10, 50)

    def activate(self, player):
        """
        Activates nest's effect on the player by raising player's targeted
        stat.

        Args:
            player: an instance of the Player
        """
        # IMPLEMENT IN PLAYER CLASS
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            player.raise_stat(self._target_stat, self._percent_increased)
