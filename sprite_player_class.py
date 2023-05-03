"""
File for player class.
"""
import pygame
from sprite_bird_class import BirdCharacter

BASE_PLAYER_HEALTH = 50000000
PLAYER_ATK = 10
PLAYER_MOVESPEED = 5
PLAYER_SCALE_IMG = 0.25


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
        _img_scale_factor: float factor by which to scale the player's image
        on the screen.
        _hp_bar_width: integer width of the HP bar
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
        # self._image = pygame.transform.scale(
        #     self._image, (self._width, self._height)
        # )
        self._img_scale_factor = PLAYER_SCALE_IMG
        self._image = pygame.transform.scale_by(
            self._image, self._img_scale_factor
        )
        self._width = self._image.get_width()
        self._height = self._image.get_height()
        self._hp_bar_width = self._width
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

    def take_damage(self, opponent_atk):
        """
        Lose an amount of HP based on opponent's ATK stat.

        Args:
            opponent_atk: an integer representing the opponent's atk stat
        """
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()
