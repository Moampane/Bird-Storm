"""
Unit tests for overarching Bird Class
"""
import pytest
from sprite_bird_class import *
from sprite_player_class import Player


"""
    Ideas:
    check that the character's hp is right after taking dmg
    check that the character's position/image updates when moved left or right
    check that the character's hp is the right width
    check character size is correct scale
"""


def test_check_hp():
    """
    Test that the character's remaining HP is set to the correct value after taking damage.
    """
    player = Player()
    initial_hp = player._remaining_hp
    opponent_atk = 10
    player.take_damage(opponent_atk)
    assert player._remaining_hp == initial_hp - opponent_atk



