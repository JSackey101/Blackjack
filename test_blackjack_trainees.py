# pylint: skip-file

"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for, points_for_card, play, get_next_card_from_deck, deal_card_to_player
from support.testing_util import player_chooses


def test_generate_deck():
    """ Tests whether the generate_deck function generates the correct cards in the correct order. """
    assert generate_deck() == ["AS", "2S", "3S", "4S",
                               "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AD", "2D", "3D", "4D",
                               "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AC", "2C", "3C", "4C",
                               "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AH", "2H", "3H", "4H",
                               "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]


def test_points_for_number_cards():
    """ Tests whether the points_for function generates the correct number of points when there are only number cards are in the hand. """
    assert points_for(["7H", "2D"]) == 9


def test_points_for_card_number():
    """ Tests whether the points_for_card function returns the correct point value for a number card. """
    assert points_for_card("7H") == 7


def test_points_for_card_face():
    """ Tests whether the points_for_card function returns the correct point value for a face card. """
    assert points_for_card("QS") == 10


def test_two_aces():
    """ Tests whether the points_for function gives a 21 when the hand is 2 Ace cards. """
    assert points_for(["AC", "AS"]) == 21


def test_hand_over_five():
    """ Tests whether the points_for function gives a 21 when there are 6 or more cards in the hand whose total does not reach 21 or above already """
    assert points_for(["1C", "2S", "3S", "4S",
                       "1H", "2C"]) == 21


def test_points_for_empty():
    """ Tests whether the points_for function gives a 0 when the input list is empty"""
    assert points_for([]) == 0


def test_points_for_number_face():
    """ Tests whether the points_for function generates the correct number of points when there are both face and number cards are in the hand. """
    assert points_for(["QH", "2D", "KS", "AH"]) == 33


def test_two_aces_plus_one():
    """ Tests whether the points_for function generates the correct number of points when the hand is 2 Aces and 1 other card. """
    assert points_for(["AH", "AS", "3H"]) == 25
