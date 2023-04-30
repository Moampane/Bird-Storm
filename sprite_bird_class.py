"""
File for overarching bird classes.
"""
import pygame


class BirdCharacter(pygame.sprite.Sprite):
    def __init__(self, image_path, screen):
        pygame.sprite.Sprite.__init__(self)
        self._image = pygame.image.load(image_path).convert_alpha()
        self._screen = screen
        self._is_facing_right = True
        self._is_facing_forward = True
        self._is_atking = False
        self._char_name = image_path.partition("_")[0]

    @property
    def image(self):
        """
        Returns the character's pygame image.
        """
        return self._image

    @property
    def rect(self):
        """
        Returns the character's pygame rectangle.
        """
        return self._rect

    @property
    def atk(self):
        """
        Returns the character's integer attack stat.
        """
        return self._atk

    def take_damage(self, opponent_atk):
        self._remaining_hp -= opponent_atk
        if self._remaining_hp <= 0:
            self.kill()

    def update(self):
        # Health bar
        hp_bar_percent = self._remaining_hp / self._max_hp * self._width
        pygame.draw.rect(
            self._screen,
            "Green",
            pygame.Rect(self._rect.x, self._rect.y - 10, hp_bar_percent, 7),
        )

    def update_img(self):
        """
        Updates the character image to be correct according to the current
        attack and heading position.
        """
        if self._is_facing_forward:
            front_or_back = "front"
        else:
            front_or_back = "back"

        if self._is_facing_right:
            left_or_right = "right"
        else:
            left_or_right = "left"

        if self._is_atking:
            atk_or_idle = "atk"
        else:
            atk_or_idle = "idle"

        updated_img_path = f"{self._char_name}_{front_or_back}_{left_or_right}_{atk_or_idle}.png"

        self._image = pygame.image.load(updated_img_path).convert_alpha()
        self._image = pygame.transform.scale(
            self._image, (self._width, self._height)
        )