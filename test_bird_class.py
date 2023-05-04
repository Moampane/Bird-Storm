"""
Unit tests for overarching Bird Class
"""
import pytest
from sprite_bird_class import *
from sprite_player_class import Player
from sprite_test_game import *


"""
    Ideas:
    check that the character's hp is right after taking dmg
    check that the character's position/image updates when moved left or right
    check that the character's hp is the right width
    check character size is correct scale
"""
test_path = "Animations/Philipe/Philipe_front_right_atk.png"


def test_check_hp():
    """
    Test that the character's remaining HP is set to the correct value after taking damage.
    """
    player = Player(image_path= test_path)
    initial_hp = player._remaining_hp
    opponent_atk = 10
    player.take_damage(opponent_atk)
    assert player._remaining_hp == initial_hp - opponent_atk



