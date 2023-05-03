"""
File for enemy classes.
"""
import pygame
import random
from sprite_bird_class import BirdCharacter
from sprite_atk_class import Attack

ENEMY_SCALE_IMG = 0.25
ENEMY_BASE_MOVESPEED = 2
ENEMY_BASE_ATK = 5
ENEMY_BASE_MAX_HP = 20


class Enemy(BirdCharacter):
    """
    A BirdCharacter class representing the enemies.
    Attributes:

    """

    def __init__(self, image_path, screen, player, tier):
        """
        Initializes instance of Enemy.

        Args:
            image_path: a string containing the file path to the images for the
            player
            screen: the surface that the game is displayed on
            player: an instance of the Player character
            tier: integer representing which tier the enemy is in; will
            determine stats based off this
        """
        super().__init__(image_path, screen)
        self._img_scale_factor = ENEMY_SCALE_IMG
        self._image = pygame.transform.scale_by(
            self._image, self._img_scale_factor
        )
        self._width = self._image.get_width()
        self._height = self._image.get_height()
        tier_multiplier = tier / 2
        self._max_hp = tier_multiplier * ENEMY_BASE_MAX_HP
        self._atk = tier_multiplier * ENEMY_BASE_ATK
        self._ms = tier_multiplier * ENEMY_BASE_MOVESPEED
        self._remaining_hp = self._max_hp
        self._start_pos = (
            random.choice([0 - self._width, screen.get_width() + self._width]),
            random.randint(0, screen.get_height() - self._height),
        )
        self._rect = self._image.get_rect(center=self._start_pos)
        self.player = player
        self._is_facing_right = True
        self._hp_bar_width = self._width
        self.atk_timer = 0

    def update(self):
        """
        Updates status of the enemy character.
        """
        super().update()
        self.atk_timer += 1

        # Initialize location data
        player_x = self.player.rect.x
        player_y = self.player.rect.y
        enemy_x = self._rect.x
        enemy_y = self._rect.y
        dist_between = 50

        # If enemy is too far left or right of player, move enemy towards
        # left or right depending on which side player is on
        if player_x > enemy_x + dist_between:
            self._is_facing_right = True
            self._rect.x += self._ms
            self._heading = 0
        elif player_x < enemy_x - dist_between:
            self._is_facing_right = False
            self._rect.x -= self._ms
            self._heading = 180

        # If enemy is too far above or below player, move enemy
        # up or down depending on which side player is on
        if player_y > enemy_y + dist_between:
            self._is_facing_forward = True
            self._rect.y += self._ms
            self._heading = 270
        elif player_y < enemy_y - dist_between:
            self._is_facing_forward = False
            self._rect.y -= self._ms
            self._heading = 90

        # update image based on heading
        self.update_img()

    def take_damage(self, opponent_atk, environment):
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()
            environment.num_enemies_slain += 1
