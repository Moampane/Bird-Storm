"""
Unit tests for overarching Bird Class
"""

from sprite_bird_class import *
from sprite_player_class import *

# from sprite_test_game import *
import pygame

"""
    Ideas:
    check that the character's hp is right after taking dmg
    check that the character's position/image updates when moved left or right
    check that the character's hp is the right width
    check character size is correct scale
"""
test_path = "Animations/Steve/Steve_front_left_atk.png"
# pygame.init()
# clock = pygame.time.Clock()

# Game Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def test_check_hp():
    """
    Test that the character's remaining HP is set to the correct value after taking damage.
    """
    bird = Player(test_path, screen1)
    initial_hp = bird._remaining_hp
    opponent_atk = 10
    bird.take_damage(opponent_atk)
    assert bird._remaining_hp == initial_hp - opponent_atk


def test_enemy_position():
    """
    The enemy should
    """


def test_animation():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(test_path, screen1)
    bird.is_facing_right() == True
    bird.set_atk_status(True)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_front_right_atk.png"
    assert actual_img_path == expected_img_path


# write out every permutation
