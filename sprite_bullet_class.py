"""
File for bullet class.
"""
import sprite_atk_class
import pygame


class Bullet(sprite_atk_class.Attack):
    def __init__(self, character, group):
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
