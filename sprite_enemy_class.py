"""
File for enemy classes.
"""
import random
import pygame
from sprite_bird_class import BirdCharacter

ENEMY_SCALE_IMG = 0.25
ENEMY_BASE_MOVESPEED = 2
ENEMY_BASE_ATK = 5
ENEMY_BASE_MAX_HP = 20


class Enemy(BirdCharacter):
    """
    A BirdCharacter class representing the enemies.

    Attributes:
        _img_scale_factor: a float representing the factor by
        which the image of the Enemy is scaled by
        _image: a pygame image representing the Enemy
        _width: an integer representing the width of the Enemy
        _height: an integer representing the height of the Enemy
        _max_hp: an integer representing the max health of the Enemy
        _atk: an integer representing the amount of damage the Enemy
        does in a single attack
        _ms: an integer representing how fast the Enemy moves across
        the screen
        _remaining_hp: an integer representing the remaining health
        of the Enemy
        _start_pos: a tuple of two integers, the first being either
        the left or right side of the screen and the second being a
        randomly chosen position between the top and bottom of the
        screen. Represents the starting position or spawn point of
        the Enemy.
        _rect: a pygame rect representing the hitbox of the Enemy
        _player: an instance of the Player character
        _is_facing_right: a boolean representing whether the Enemy
        is facing right or not
        _atk_timer: an integer representing the Enemy's internal timer
        used to determine when to attack

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
        self._hp_bar_width = self._width
        tier_multiplier = tier
        self._max_hp = tier_multiplier * ENEMY_BASE_MAX_HP
        self._atk = tier_multiplier * ENEMY_BASE_ATK
        self._ms = tier_multiplier * ENEMY_BASE_MOVESPEED
        self._remaining_hp = self._max_hp
        self._start_pos = (
            random.choice([0 - self._width, screen.get_width() + self._width]),
            random.randint(0, screen.get_height() - self._height),
        )
        self._rect = self._image.get_rect(center=self._start_pos)
        self._player = player
        self._is_facing_right = True
        self._atk_timer = 0

    def update(self):
        """
        Updates status of the enemy character.
        """
        super().update()
        self._atk_timer += 1

        # Initialize location data
        player_x = self._player.rect.x
        player_y = self._player.rect.y
        enemy_x = self._rect.x
        enemy_y = self._rect.y
        dist_between = 100

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
        """
        Makes enemy take damage and updates environment's num_enemies_slain.
        Args:
            opponent_atk: an integer representing the opponent's atk stat
            environment: an Environment object representing the game
            environment.
        """
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()
            environment.num_enemies_slain += 1

    @property
    def atk_timer(self):
        """
        Returns the integer representing the Enemy attack timer.
        """
        return self._atk_timer
