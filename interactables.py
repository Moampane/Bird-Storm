"""
File for the Interactables class.
"""
from abc import ABC, abstractmethod
import pygame


class Interactables(ABC):
    """
    Abstract base class representing any interactable object on the screen.

    Attributes:
        _img_path: a string representing the file path to the folder
        containing the object's image
        _img: a pygame surface containing the image of the object
        _img_rect: a pygame rectangle mapped to the object image
    """

    def __init__(self, img_path):
        """
        Base initialization function for all Interactable subclass instances.
        Will be implemented for each subclass.

        Args:
            img_path: a string representing the file path to the object images
        """
        self._img_path = img_path
        self._img = pygame.image.load(img_path).convert_alpha()
        self._img_rect = pygame.transform.scale(self._img, (50, 50))

    def check_interact(self, player):
        """
        Checks if the player is touching the interactable.

        Args:
            player: an instance of Player representing the player's character.
        Returns:
            A boolean representing whether the player is touching the
            interactable or not.
        """
        if self._img_rect.colliderect(player.sprite_rect):
            return True
        return False

    @abstractmethod
    def activate(self, player):
        """
        Base function for activating interactable's effect on the player. WIll
        be implemented in Interactable's subclasses.

        Args:
            player: an instance of the Player
        """

    def draw(self, screen, player):
        """
        Draws the interactable on the screen and checks all interactions
        with the player.

        Args:
            screen: the pygame display surface
            player: an instance of the Player class representing the player's
            character
        """
        screen.blit(self._img, self._img_rect)

        if self.check_interact(player):
            self.activate(player)
