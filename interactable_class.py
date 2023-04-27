"""
File for the Interactable class.
"""
import pygame
import random
from abc import ABC, abstractmethod

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class Interactable(ABC):
    """
    Abstract base class representing any interactable object on the screen.

    Attributes:
        _img_path: a string representing the file path to the folder
        containing the object's image
        _img: a pygame surface containing the image of the object
        _img_rect: a pygame rectangle mapped to the object image
        _spawn_loc: a tuple containing the x and y spawn location of the
        interactable
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
        self._img = pygame.transform.scale(self._img, (50, 50))
        self._img_rect = self._img.get_rect()
        self._spawn_loc = (
            random.randint(0, WINDOW_WIDTH - self._img_rect.width),
            random.randint(0, WINDOW_HEIGHT - self._img_rect.height),
        )
        self._img_rect = self._img.get_rect(center=self._spawn_loc)

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
            # CHANGE IMAGE TO HIGHLIGHT IN YELLOW AND DISPLAY PROMPT TO PICK UP
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
