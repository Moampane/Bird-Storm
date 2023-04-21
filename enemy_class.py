"""
File for the bird enemies classes.
"""

import random
import pygame
from bird_class import BirdCharacter

BASE_ENEMY_HP = 100
BASE_ENEMY_ATK = 10
BASE_ENEMY_SPD = 1


class EnemyBird(BirdCharacter):
    """
    Attributes:

        _spawn_loc: a list containing the x and y spawn location of the enemy
    """

    def __init__(self, sprite_path):
        super().__init__(sprite_path)
        self._max_hp = BASE_ENEMY_HP
        self._remaining_hp = BASE_ENEMY_HP
        self._atk = BASE_ENEMY_ATK

        # change to variables containing window size
        # also change logic to do the entire border around window
        self._spawn_loc = [random.choice([0, 800]), random.randint(0, 800)]
        self._sprite_img = pygame.transform.scale(self._sprite_img, (100, 100))

    def follow_player(self, player):
        """
        Updates enemy location to follow the player's location.

        Args:
            player: an instance of BirdPlayer that represents the player.
        Returns:
            A list containing the updated x and y coordinates of the enemy
            according to the player's position.
        """
        player_x = player.sprite_rect.x
        player_y = player.sprite_rect.y
        enemy_x = self._sprite_rect.x
        enemy_y = self._sprite_rect.y

        if player_x > enemy_x:
            self._sprite_rect.x += BASE_ENEMY_SPD
        elif player_x < enemy_x:
            self._sprite_rect.x -= BASE_ENEMY_SPD

        if player_y > enemy_y:
            self._sprite_rect.y += BASE_ENEMY_SPD
        elif player_y < enemy_y:
            self._sprite_rect.y -= BASE_ENEMY_SPD

    def _die(self):
        """
        Die
        """
        # will implement later
        pass


class BossEnemyBird(EnemyBird):
    """
    Attributes:

    """

    def __init__(self, sprite_path):
        super().__init__(sprite_path)
        self._max_hp = 10 * BASE_ENEMY_HP
        self._remaining_hp = self._max_hp
        self._atk = 5 * BASE_ENEMY_ATK
        self._spawn_loc = [0, 0]
