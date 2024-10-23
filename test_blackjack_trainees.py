# pylint: skip-file

"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for, play, get_next_card_from_deck, deal_card_to_player
from support.testing_util import player_chooses


def test_get_next_hand_one():
    """tests get_next_card_from_deck with a right answer"""
    assert get_next_card_from_deck(['5H', '8C', 'QS', 'AH']) == '5H'


def test_get_next_hand_two():
    """tests get_next_card_from_deck with a right answer and a list of one"""
    assert get_next_card_from_deck(['5H']) == '5H'


def test_deal_card_to_hand():
    """tests deal_card_to_hand with a correct answer"""
    player = {'hand': ['KH']}
    assert deal_card_to_player(['7H', 'KC', '2S'], ['KH']) == {
        'hand': ['KH', '7H']}


def test_deal_card_to_hand_two():
    """tests deal_card_to_hand with a correct answer"""
    player = {'hand': ['3H', '4S']}
    assert deal_card_to_player(['7S', '3C', 'JH', 'KS'], [
        '3H', '4S']) == {'hand': ['3H', '4S', '7S']}
