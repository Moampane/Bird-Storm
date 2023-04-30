"""
File for player classes.
"""
import pygame
from sprite_bird_class import BirdCharacter

BASE_PLAYER_HEALTH = 1000
PLAYER_ATK = 5
PLAYER_MOVESPEED = 5
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100


class Player(BirdCharacter):
    """
    A class representing the BirdCharacter Player.

    Attributes:
        _max_hp: an integer representing the max health of the player
        _remaining_hp: an integer representing the remaining health
        of the player
        _atk: an integer representing the amount of damage the player
        does in a single attack
        _ms: an integer representing how fast the player moves across
        the screen
        _width: an integer representing the width of the player image
        _height: an integer representing the height of the player
        image
        _image: a pygame image representing the image of the player
        _start_pos: a tuple containing the (x,y) starting position
        of the player
        _rect: a pygame rectangle mapped to the player's image
        _screen: the surface that the game is displayed on
        _is_facing_right: a boolean representing if the player is facing
        right
        _is_facing_forward: a boolean representing if the player is
        facing forward
        _is_atking: a boolean representing if the player is attacking
        _char_name: a string representing the first section of the player
        image file path
        _heading: an integer representing the heading of the player
    """

    def __init__(self, image_path, screen):
        """
        Initializes an instance of the Player.
        Args:
            image_path: a string containing the file path to the images for the
            player
            screen: the surface that the game is displayed on
        """
        super().__init__(image_path, screen)
        self._max_hp = BASE_PLAYER_HEALTH
        self._remaining_hp = self._max_hp
        self._atk = PLAYER_ATK
        self._ms = PLAYER_MOVESPEED
        self._width = PLAYER_WIDTH
        self._height = PLAYER_HEIGHT
        self._image = pygame.transform.scale(
            self._image, (self._width, self._height)
        )
        self._start_pos = (
            screen.get_width() / 2,
            screen.get_height() - self._height / 2,
        )
        self._rect = self._image.get_rect(center=self._start_pos)

    def update(self):
        """
        Updates current state of player based on keyboard inputs.
        """
        super().update()
        keys = pygame.key.get_pressed()

        # player movement
        if keys[pygame.K_a]:
            self._rect.x -= self._ms
            self._is_facing_right = False
            self._heading = 180
        if keys[pygame.K_d]:
            self._rect.x += self._ms
            self._is_facing_right = True
            self._heading = 0
        if keys[pygame.K_w]:
            self._rect.y -= self._ms
            self._is_facing_forward = False
            self._heading = 90
        if keys[pygame.K_s]:
            self._rect.y += self._ms
            self._is_facing_forward = True
            self._heading = 270

        self.update_img()
