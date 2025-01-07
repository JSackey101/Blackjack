# pylint: skip-file

"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for, play, get_next_card_from_deck, deal_card_to_player
from support.testing_util import player_chooses


def test_generate_deck():
    assert generate_deck() == ["AS", "2S", "3S", "4S",
                               "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AD", "2D", "3D", "4D",
                               "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AC", "2C", "3C", "4C",
                               "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AH", "2H", "3H", "4H",
                               "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]


def test_points_for():
    assert points_for(["7H", "2D"]) == 9


def test_two_aces():
    assert points_for(["AC", "AS"]) == 21


def test_hand_over_five():
    assert points_for(["1C", "2S", "3S", "4S",
                       "1H", "2C"]) == 21
