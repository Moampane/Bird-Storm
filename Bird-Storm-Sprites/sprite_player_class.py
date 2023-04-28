"""
File for player classes.
"""
import pygame
from sprite_bird_class import BirdCharacter

BASE_PLAYER_HEALTH = 1000
PLAYER_ATK = 5
PLAYER_MOVESPEED = 5
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100


class Player(BirdCharacter):
    """
    A class representing the BirdCharacter Player.

    Attributes:
        self._max_hp: an integer representing the max health of the player
        self._remaining_hp: an integer representing the remaining health
        of the player
        self._atk: an integer representing the amount of damage the player
        does in a single attack
        self._ms: an integer representing how fast the player moves across
        the screen
        self._width: an integer representing the width of the player image
        self._height: an integer representing the height of the player
        image
        self._image: a pygame image representing the image of the player
        self._start_pos: a tuple containing the (x,y) starting position
        of the player
        self._rect: a pygame rectangle mapped to the player's image
        self._screen: the surface that the game is displayed on
        self._is_facing_right: a boolean representing if the player is facing
        right
        self._is_facing_forward: a boolean representing if the player is
        facing forward
        self._is_atking: a boolean representing if the player is attacking
        self._char_name: a string representing the first section of the player
        image file path
        self._player_heading: an integer representing the heading of the player
    """

    def __init__(self, image_path, screen):
        """
        Initializes an instance of the Player.
        Args:
            image_path: a string containing the file path to the images for the
            player
            screen: the surface that the game is displayed on
        """
        super().__init__(image_path, screen)
        self._max_hp = BASE_PLAYER_HEALTH
        self._remaining_hp = self._max_hp
        self._atk = PLAYER_ATK
        self._ms = PLAYER_MOVESPEED
        self._width = PLAYER_WIDTH
        self._height = PLAYER_HEIGHT
        self._image = pygame.transform.scale(self._image, (self._width, self._height))
        self._start_pos = (
            screen.get_width() / 2,
            screen.get_height() - self._height / 2,
        )
        self._rect = self._image.get_rect(center=self._start_pos)
        self._is_facing_right = True
        self._is_facing_forward = True
        self._is_atking = False
        self._char_name = image_path.partition("_")[0]
        self._player_heading = 0

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

        updated_img_path = (
            f"{self._char_name}_{front_or_back}_{left_or_right}_{atk_or_idle}.png"
        )

        self._image = pygame.image.load(updated_img_path).convert_alpha()
        self._image = pygame.transform.scale(self._image, (self._width, self._height))

    def update(self):
        """
        Updates current state of player based on keyboard inputs.
        """
        super().update()
        keys = pygame.key.get_pressed()

        # player movement
        if keys[pygame.K_a]:
            self._rect.x -= self._ms
            self._is_facing_right = False
            self._player_heading = 180
        if keys[pygame.K_d]:
            self._rect.x += self._ms
            self._is_facing_right = True
            self._player_heading = 0
        if keys[pygame.K_w]:
            self._rect.y -= self._ms
            self._is_facing_forward = False
            self._player_heading = 90
        if keys[pygame.K_s]:
            self._rect.y += self._ms
            self._is_facing_forward = True
            self._player_heading = 270

        self.update_img()

    @property
    def player_heading(self):
        """
        Returns the player_heading of a Player object.
        """
        return self._player_heading


class Attack(pygame.sprite.Sprite):
    """
    Class representing the player's attack.

    Attributes:
        _player: A Player object representing the player's character.
        _image: A pygame image representing the player's attack animation.
        _rect: A pygame rectangle mapped to the attack's image
        _animation_loop: An int representing the frame the animation is on.
    """

    def __init__(self, character, group):
        """
        Constructor for Attack class.

        Args:
            character: A Player object representing the player's character.
            Assigned to _player attribute.
            group: A pygame sprite group holding the Attack object.
        """
        super().__init__()
        group.add(self)
        self._player = character
        self._image = pygame.image.load("graphics/bite.png")
        self._image = pygame.transform.scale(self._image, (100, 100))
        self._rect = self._image.get_rect(center=(-1000, -1000))
        self._animation_loop = 0

    def update(self):
        if self._player.player_heading == 0:
            self._rect = self._image.get_rect(
                center=(self._player.rect.x + 150, self._player.rect.y + 50)
            )
        if self._player.player_heading == 90:
            self._rect = self._image.get_rect(
                center=(self._player.rect.x + 50, self._player.rect.y - 50)
            )
        if self._player.player_heading == 180:
            self._rect = self._image.get_rect(
                center=(self._player.rect.x - 50, self._player.rect.y + 50)
            )
        if self._player.player_heading == 270:
            self._rect = self._image.get_rect(
                center=(self._player.rect.x + 50, self._player.rect.y + 150)
            )
        self._animation_loop += 0.5
        if self._animation_loop >= 5:
            self.kill()

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect
