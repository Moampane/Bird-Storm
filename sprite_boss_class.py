import pygame
import random
from sprite_bird_class import BirdCharacter


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
        self._is_facing_right = True
        self._new_pos = random.choice(
            ["center", "bottom left", "bottom right", "top left", "top right"]
        )
        self._hp_bar_width = self._width

    def take_damage(self, opponent_atk, environment):
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()
            environment.set_boss_slain_true()

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

        if not self.incomplete_intro:
            if timer % 100 == 0:
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

    def move_to_pos(self, new_pos):
        """
        Moves boss enemy to the new position based on what string position
        is inputted.

        Args:
            new_pos: a string input representing the new location
        """
        EDGE_GAP = 0

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
            if not self._is_facing_right:
                self._image = pygame.transform.flip(self._image, True, False)
                self._is_facing_right = True
            self._rect.x += self._ms
        elif new_x < self.rect.x:
            if self._is_facing_right:
                self._image = pygame.transform.flip(self._image, True, False)
                self._is_facing_right = False
            self._rect.x -= self._ms

        if new_y > self.rect.y:
            self._rect.y += self._ms
        elif new_y < self.rect.y:
            self._rect.y -= self._ms
