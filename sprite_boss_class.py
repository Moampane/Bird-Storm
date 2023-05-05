"""
File for ProjectileBoss class.
"""
import random
import pygame
from sprite_bird_class import BirdCharacter
from sprite_bullet_class import Bullet

BOSS_IMG_SCALE = 0.45
BOSS_MAX_HEALTH = 200
BOSS_ATTACK = 0.5
BOSS_MOVESPEED = 4


class ProjectileBoss(BirdCharacter):
    """
    A class representing the BirdCharacter Boss.

    Attributes:
        _max_hp: an integer representing the max health of the Boss
        _atk: an integer representing the amount of damage the Boss
        does in a single attack
        _ms: an integer representing how fast the Boss moves across
        the screen
        _remaining_hp: an integer representing the remaining health
        of the Boss
        _player: an instance of the Player character
        _incomplete_intro: a boolean representing whether the
        introduction is incomplete or not
        _img_scale_factor: a float representing the factor by
        which the image of the boss is scaled by
        _image: a pygame image representing the Boss
        _width: an integer representing the width of the Boss
        _height: an integer representing the height of the Boss
        _rect: a pygame rect representing the hitbox of the Boss
        _is_facing_right: a boolean representing whether the Boss
        is facing right or not
        _new_pos: a String representing the next location the Boss
        will move to
        _timer: an integer representing the Boss' internal timer
        _hp_bar_width: An integer representing the width of the hp bar.
        _bullet_group: A pygame sprite group containing sprites representing
        the Boss' bullets.
        _atk_timer: An integer representing the Boss' internal timer
        specifically for displaying the attack graphic.
        _disable_bounds: A boolean representing whether the Boss can be
        outside of bounds or not.
    """

    def __init__(self, image_path, bg, player, bullet_group):
        """
        Initializes instance of ProjectileBoss

        Args:
            image_path: a string containing the file path to the images for the
            player
            bg: the surface that the game is displayed on
            player: an instance of the Player character
            bullet_group: A pygame sprite group containing sprites representing
            the Boss' bullets.
        """
        super().__init__(image_path, bg)
        self._max_hp = BOSS_MAX_HEALTH
        self._atk = BOSS_ATTACK
        self._ms = BOSS_MOVESPEED
        self._remaining_hp = self._max_hp
        self._player = player
        self._img_scale_factor = BOSS_IMG_SCALE
        self._image = pygame.transform.scale_by(
            self._image, self._img_scale_factor
        )
        self._width = self._image.get_width()
        self._height = self._image.get_height()
        start_pos = (self._screen.get_width() / 2, -200)
        self._rect = self._image.get_rect(center=start_pos)
        self._is_facing_right = True
        self._new_pos = random.choice(
            ["center", "bottom left", "bottom right", "top left", "top right"]
        )
        self._incomplete_intro = True
        self._timer = 0
        self._hp_bar_width = self._width
        self._bullet_group = bullet_group
        self._atk_timer = 0
        self._disable_bounds = True

    def take_damage(self, opponent_atk, environment):
        """
        Lose an amount of HP based on opponent's ATK stat.

        Args:
            opponent_atk: an integer representing the opponent's atk stat
            environment: an Environment object representing the game
            environment.
        """
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()
            environment.set_boss_slain_true()

    def bullet_spray(self):
        """
        Shoots 8 bullets in different directions around the boss.
        """
        move_x_vals = [0, 1, 1, 1, 0, -1, -1, -1]
        move_y_vals = [-1, -1, 0, 1, 1, 1, 0, -1]
        screen_width, screen_height = self.screen.get_size()
        for idx in range(8):
            Bullet(
                self,
                self._bullet_group,
                (move_x_vals[idx], move_y_vals[idx]),
                (screen_width, screen_height),
            )

    def update(self):
        """
        Updates status of Boss.
        """
        super().update()

        # Boss intro
        if (
            self._rect.y < self._screen.get_height() / 2 - 100
            and self._incomplete_intro
            and self._timer % 10 == 0
        ):
            # change back to 1 later
            # Moves boss
            self._rect.y += 40
            # Forces player in place
            self._player.rect.x = self._player.width
            self._player.rect.y = (
                self._screen.get_height() / 2 - self._player.height / 2
            )
            self._player.control_movement(False)
            # Ends intro
            if self._rect.y >= self._screen.get_height() / 2 - 100:
                self._disable_bounds = False
                self._incomplete_intro = False
                self._player.control_movement(True)

        # Randomly choose Boss movement
        if not self._incomplete_intro:
            if self._timer % 200 == 0:
                self.set_atk_status(True)
                self._atk_timer = 0
                self._new_pos = random.choice(
                    [
                        "center",
                        "bottom left",
                        "bottom right",
                        "top left",
                        "top right",
                    ]
                )
                self.bullet_spray()
            self.move_to_pos(self._new_pos)
            if self._atk_timer == 50:
                self.set_atk_status(False)
        self.update_img()

        # increment timer
        self._timer += 1
        self._atk_timer += 1

    def move_to_pos(self, new_pos):
        """
        Moves boss enemy to the new position based on what string position
        is inputted.

        Args:
            new_pos: a string input representing the new location
        """
        edge_gap = 0

        if "bottom" in new_pos:
            new_y = self._screen.get_height() - self._height - edge_gap
        else:
            new_y = edge_gap

        if "left" in new_pos:
            new_x = edge_gap
        else:
            new_x = self._screen.get_width() - self._width - edge_gap

        if new_pos == "center":
            new_x = self._screen.get_width() / 2 - self._width / 2
            new_y = self._screen.get_height() / 2 - self._height / 2

        if new_x > self.rect.x:
            self._is_facing_right = True
            self._rect.x += self._ms
        elif new_x < self.rect.x:
            self._is_facing_right = False
            self._rect.x -= self._ms

        if new_y > self.rect.y:
            self._rect.y += self._ms
        elif new_y < self.rect.y:
            self._rect.y -= self._ms
