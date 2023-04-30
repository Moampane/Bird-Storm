"""
File for enemy classes.
"""
import pygame
import random
from sprite_bird_class import BirdCharacter

ENEMY_WIDTH = 100
ENEMY_HEIGHT = 100
ENEMY_MOVESPEED = 2
ENEMY_ATK = 10
ENEMY_BASE_MAX_HP = 20


class Enemy(BirdCharacter):
    """
    A BirdCharacter class representing the enemies.
    Attributes:

    """

    def __init__(self, image_path, screen, player):
        """
        Initializes instance of Enemy.

        Args:
            image_path: a string containing the file path to the images for the
            player
            screen: the surface that the game is displayed on
            player: an instance of the Player character
        """
        super().__init__(image_path, screen)
        self._width = ENEMY_WIDTH
        self._height = ENEMY_HEIGHT
        self._image = pygame.transform.scale(
            self._image, (self._width, self._height)
        )
        self._max_hp = ENEMY_BASE_MAX_HP
        self._atk = ENEMY_ATK
        self._ms = ENEMY_MOVESPEED
        self._remaining_hp = self._max_hp
        self._start_pos = (
            random.choice([0 - self._width, screen.get_width() + self._width]),
            random.randint(0, screen.get_height() - self._height),
        )
        self._rect = self._image.get_rect(center=self._start_pos)
        self.player = player
        self._is_facing_right = True

    def update(self):
        """
        Updates status of the enemy character.
        """
        super().update()

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


class Projectile_Boss(BirdCharacter):
    def __init__(
        self,
        max_health,
        attack,
        movespeed,
        image_path,
        start_pos,
        size,
        bg,
        player,
    ):
        super().__init__(image_path, bg)
        self._width = size[0]
        self._height = size[1]
        self._max_hp = max_health
        self._atk = attack
        self._ms = movespeed
        self._remaining_hp = self._max_hp
        self.player = player
        self.incomplete_intro = True
        self.position = "center"
        self._image = pygame.image.load(image_path).convert_alpha()
        self._image = pygame.transform.scale(
            self._image, (self._width, self._height)
        )
        self._rect = self._image.get_rect(center=start_pos)
        self.complete_move = False
        self.is_facing_right = True
        self._new_pos = random.choice(
            ["center", "bottom left", "bottom right", "top left", "top right"]
        )

    def take_damage(self, opponent_atk, environment):
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()
            environment.num_enemies_slain += 100

    def update(self, timer):
        super().update()

        if (
            self._rect.y < self._screen.get_height() / 2 - 100
            and self.incomplete_intro
            and timer % 10 == 0
        ):
            # change back to 1 later
            # Moves boss
            self._rect.y += 40
            # Forces player in place
            self.player.rect.y = self._screen.get_height() - 100
            self.player.rect.x = self._screen.get_width() / 2 - 50
            # Ends intro
            if self._rect.y >= self._screen.get_height() / 2 - 100:
                self.incomplete_intro = False

        # if not self.incomplete_intro and self.timer % 100 == 0:
        # self.go_to_top_left()
        # self.go_to_top_right()
        # self.go_to_bottom_left()
        # self.go_to_bottom_right()
        if not self.incomplete_intro:
            if timer % 250 == 0:
                self._new_pos = random.choice(
                    [
                        "center",
                        "bottom left",
                        "bottom right",
                        "top left",
                        "top right",
                    ]
                )
            self.move_to_pos(self._new_pos)

    def move_to_pos(self, new_pos=""):
        """
        Moves boss enemy to the new position based on what string position
        is inputted.

        Args:
            new_pos: a string input representing the new location
        """
        EDGE_GAP = 20

        if new_pos == "":
            return

        if "bottom" in new_pos:
            new_y = self._screen.get_height() - self._height - EDGE_GAP
        else:
            new_y = EDGE_GAP

        if "left" in new_pos:
            new_x = EDGE_GAP
        else:
            new_x = self._screen.get_width() - self._width - EDGE_GAP

        if new_pos == "center":
            new_x = self._screen.get_width() / 2 - self._width / 2
            new_y = self._screen.get_height() / 2 - self._height / 2

        if new_x > self.rect.x:
            if not self.is_facing_right:
                self._image = pygame.transform.flip(self._image, True, False)
                self.is_facing_right = True
            self._rect.x += self._ms
        elif new_x < self.rect.x:
            if self.is_facing_right:
                self._image = pygame.transform.flip(self._image, True, False)
                self.is_facing_right = False
            self._rect.x -= self._ms

        if new_y > self.rect.y:
            self._rect.y += self._ms
        elif new_y < self.rect.y:
            self._rect.y -= self._ms
