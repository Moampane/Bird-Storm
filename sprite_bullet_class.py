"""
File for bullet class.
"""
import pygame
import sprite_atk_class


BULLET_SPEED = 7
BULLET_DAMAGE = 10
BULLET_PATH = "Animations/egg_projectile.png"
BULLET_SCALE = 0.2


class Bullet(sprite_atk_class.Attack):
    """
    Class representing a character's bullet attack.

    Attributes:
         _character: A BirdCharacter instance representing the attacking
        character.
        _image: A pygame image representing the character's attack hitbox.
        _rect: A pygame rectangle mapped to the attack's image.
        _first_hit: A boolean representing whether the first hit has
        occurred or not.
        _move_x: An integer, either -1, 0, or 1, representing the direction
        of x displacement.
        _move_y: An integer, either -1, 0, or 1, representing the direction
        of y displacement.
        _screen_width: An integer representing the width of the screen.
        _screen_height: An integer representing the height of the screen.
        _damage: An integer representing the damage dealt by a bullet.
    """

    def __init__(self, character, group, displacement, bg_size):
        """
        Constructor for Bullet class.

        Args:
            character: A BirdCharacter instance representing the attacking
            character.
            group: A pygame sprite group holding the Bullet object.
            displacement: A tuple representing the direction of movement
            of the bullet. The first element represents the x direction
            and the second the y direction.
            bg_size: A tuple representing the size of the screen. The first
            element represents the width of the screen and the second the
            height.
        """
        super().__init__(character, group)
        self._image = pygame.image.load(BULLET_PATH).convert_alpha()
        self._image = pygame.transform.scale_by(self._image, BULLET_SCALE)
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
        self._move_x = displacement[0]
        self._move_y = displacement[1]
        self._screen_width = bg_size[0]
        self._screen_height = bg_size[1]
        self._damage = BULLET_DAMAGE

    def shoot(self):
        """
        Moves bullet
        """
        # change in x
        self._rect.x += self._move_x * BULLET_SPEED
        # change in y
        self._rect.y += self._move_y * BULLET_SPEED

    def update(self):
        """
        Updates bullet position and existence based on whether or not bullet
        is within the screen.
        """
        # moves bullet
        self.shoot()
        # if bullet goes out of bounds remove it
        BOUNDS_SPACING = 100
        if (
            self._rect.x > self._screen_width + BOUNDS_SPACING
            or self._rect.x < -BOUNDS_SPACING
            or self._rect.y < -BOUNDS_SPACING
            or self._rect.y > self._screen_height + BOUNDS_SPACING
        ):
            self.kill()

    @property
    def damage(self):
        """
        Returns the integer of damage.
        """
        return self._damage
