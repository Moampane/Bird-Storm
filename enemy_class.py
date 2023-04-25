"""
File for the bird enemies classes.
"""

import random
import pygame
from bird_class import BirdCharacter

BASE_ENEMY_HP = 100
BASE_ENEMY_ATK = 5
BASE_ENEMY_SPD = 2

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class EnemyBird(BirdCharacter):
    """
    Attributes:

        _spawn_loc: a list containing the x and y spawn location of the enemy
        _is_facing_right = a boolean telling if the enemy is facing right
        _atk_interval_tracker = integer used for spacing out enemy attacks
    """

    def __init__(self, sprite_path):
        """
        Initializes instance of EnemyBird.

        Args:
            sprite_path: a string representing the file path to the character
            sprite images
        """
        # Set up stats and basic info
        self._max_hp = BASE_ENEMY_HP
        self._remaining_hp = BASE_ENEMY_HP
        self._atk = BASE_ENEMY_ATK
        self._is_facing_right = True
        self._is_dead = False
        self._atk_interval_tracker = 0

        # Set up sprite images and rectangles
        self._sprite_path = sprite_path
        self._sprite_img = pygame.image.load(sprite_path).convert_alpha()
        self._sprite_img = pygame.transform.scale(self._sprite_img, (100, 100))
        self._sprite_rect = self._sprite_img.get_rect()

        # Randomize spawn location to either the left or right side of the
        # screen at a random y coordinate
        self._spawn_loc = (
            random.choice([0, WINDOW_WIDTH - self._sprite_rect.width]),
            random.randint(0, WINDOW_HEIGHT - self._sprite_rect.height),
        )
        self._sprite_rect = self._sprite_img.get_rect(topleft=self._spawn_loc)

    def follow_player(self, player):
        """
        Updates enemy location to follow the player's location.

        Args:
            player: an instance of Player that represents the player.
        """
        player_x = player.sprite_rect.x
        player_y = player.sprite_rect.y
        enemy_x = self._sprite_rect.x
        enemy_y = self._sprite_rect.y
        dist_between = 50

        # If enemy is too far left or right of player, move enemy towards
        # left or right depending on which side player is on and flip enemy
        # sprite towards the direction player is in
        if player_x > enemy_x + dist_between:
            if not self._is_facing_right:
                self._sprite_img = pygame.transform.flip(self._sprite_img, True, False)
                self._is_facing_right = True
            self._sprite_rect.x += BASE_ENEMY_SPD
        elif player_x < enemy_x - dist_between:
            if self._is_facing_right:
                self._sprite_img = pygame.transform.flip(self._sprite_img, True, False)
                self._is_facing_right = False
            self._sprite_rect.x -= BASE_ENEMY_SPD

        # If enemy is too far above or below player, move enemy
        # up or down depending on which side player is on
        if player_y > enemy_y + dist_between:
            self._sprite_rect.y += BASE_ENEMY_SPD
        elif player_y < enemy_y - dist_between:
            self._sprite_rect.y -= BASE_ENEMY_SPD

    def _die(self):
        """
        Makes enemy disappear from the screen when their remaining HP reaches
        0.
        """
        if self._remaining_hp <= 0:
            self._sprite_img = pygame.transform.rotate(self._sprite_img, 90)
            self._is_dead = True

    def draw(self, screen, player, test):
        # DEELTE TEST LATER
        """
        Draws the character and associated information on the screen.

        Args:
            screen: the pygame display surface
            player: an instance of the Player class representing the player's
            character
        """
        # If enemy is dead, don't execute function
        if self._is_dead:
            return

        # Draw enemy on the screen
        screen.blit(self._sprite_img, self._sprite_rect)

        # Draw HP bar a bit above enemy location
        percent_hp_remain_bar = (
            self._remaining_hp / self._max_hp
        ) * self._sprite_rect.width
        pygame.draw.rect(
            screen,
            "Red",
            pygame.Rect(
                self.sprite_rect.x, self.sprite_rect.y - 10, percent_hp_remain_bar, 7
            ),
        )

        # DELETE LATER
        if test:
            return

        # Enemy attack logic with spaced out attacks
        self._atk_interval_tracker += 1
        if self._atk_interval_tracker % 100 == 0:
            self.attack(player)

        # Enemy follow the player on screen
        self.follow_player(player)


class BossEnemyBird(EnemyBird):
    """
    Attributes:

    """

    def __init__(self, sprite_path):
        super().__init__(sprite_path)
        self._max_hp = 10 * BASE_ENEMY_HP
        self._remaining_hp = self._max_hp
        self._atk = 5 * BASE_ENEMY_ATK
        self._spawn_loc = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]
        self._sprite_img = pygame.transform.scale(self._sprite_img, (300, 300))
        self._sprite_rect = self._sprite_img.get_rect(center=self._spawn_loc)
