"""
File for bullet class.
"""
import pygame
import sprite_atk_class


BULLET_SPEED = 5
BULLET_DAMAGE = 25


class Bullet(sprite_atk_class.Attack):
    def __init__(self, character, group, move_x, move_y, bg_width, bg_height):
        super().__init__(character, group)
        self._image = pygame.Surface((50, 50))
        self._image.fill((255, 0, 0))
        character_x = character.rect.x
        character_y = character.rect.y
        character_width = character.width
        character_height = character.height
        self._rect = self._image.get_rect(
            center=(
                character_x + character_width / 2,
                character_y + character_height / 2,
            )
        )
        self._move_x = move_x
        self._move_y = move_y
        self._screen_width = bg_width
        self._screen_height = bg_height
        self._damage = BULLET_DAMAGE

    def shoot(self):
        # change in x
        self._rect.x += self._move_x * BULLET_SPEED
        # change in y
        self._rect.y += self._move_y * BULLET_SPEED

    # def set_x_speed(self, x_speed):
    #     self._x_speed = x_speed

    # def set_y_speed(self, y_speed):
    #     self._y_speed = y_speed

    def update(self):
        self.shoot()
        # if bullet goes out of bounds remove it
        if (
            self._rect.x > self._screen_width - 50
            or self._rect.x < 50
            or self._rect.y < 50
            or self._rect.y > self._screen_height - 50
        ):
            self.kill()

    @property
    def damage(self):
        """
        Returns the integer of damage.
        """
        return self._damage
