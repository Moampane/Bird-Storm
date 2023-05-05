"""
Unit tests for overarching Bird Class
"""

from sprite_bird_class import *
from sprite_player_class import *
import pygame

TEST_PATH = "Animations/Steve/Steve_front_left_idle.png"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def test_check_hp():
    """
    Test that the character's remaining HP is set to the correct value after taking damage.
    """
    bird = Player(TEST_PATH, screen1)
    initial_hp = bird.remaining_hp
    opponent_atk = 10
    bird.take_damage(opponent_atk)
    assert bird.remaining_hp == initial_hp - opponent_atk


def test_stay_in_bounds():
    """
    Test that the player stays within bounds when screen updates
    """
    bird = Player(TEST_PATH, screen1)
    bird.update()
    assert bird._disable_bounds == False


def test_hp_length():
    """
    Check that the hp length is only equal to the character's idle animation png width
    """
    bird = Player(TEST_PATH, screen1)
    idle_image = pygame.image.load(TEST_PATH)
    idle_width = idle_image.get_width()
    idle_width = idle_width * PLAYER_SCALE_IMG
    assert abs(bird._hp_bar_width - idle_width) <= 1


def test_animation_front_right_atk():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(TEST_PATH, screen1)
    bird._is_facing_right = True
    bird._is_facing_forward = True
    bird.set_atk_status(True)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_front_right_atk.png"
    assert actual_img_path == expected_img_path


def test_animation_front_left_atk():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(TEST_PATH, screen1)
    bird._is_facing_right = False
    bird._is_facing_forward = True
    bird.set_atk_status(True)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_front_left_atk.png"
    assert actual_img_path == expected_img_path


def test_animation_back_left_atk():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(TEST_PATH, screen1)
    bird._is_facing_forward = False
    bird._is_facing_right = False
    bird.set_atk_status(True)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_back_left_atk.png"
    assert actual_img_path == expected_img_path


def test_animation_back_right_atk():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(TEST_PATH, screen1)
    bird._is_facing_forward = False
    bird._is_facing_right = True
    bird.set_atk_status(True)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_back_right_atk.png"
    assert actual_img_path == expected_img_path


def test_animation_front_right_idle():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(TEST_PATH, screen1)
    bird._is_facing_forward = True
    bird._is_facing_right = True
    bird.set_atk_status(False)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_front_right_idle.png"
    assert actual_img_path == expected_img_path


def test_animation_back_right_idle():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(TEST_PATH, screen1)
    bird._is_facing_forward = False
    bird._is_facing_right = True
    bird.set_atk_status(False)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_back_right_idle.png"
    assert actual_img_path == expected_img_path


def test_animation_back_left_idle():
    """
    Test that the character's animation is mapped to the correct image
    """
    bird = Player(TEST_PATH, screen1)
    bird._is_facing_forward = False
    bird._is_facing_right = False
    bird.set_atk_status(False)
    actual_img_path = bird.update_img()
    expected_img_path = "Animations/Steve/Steve_back_left_idle.png"
    assert actual_img_path == expected_img_path
