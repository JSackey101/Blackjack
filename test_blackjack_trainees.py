# pylint: skip-file

"""File for tests written by you - the trainee"""

from blackjack import generate_deck, points_for, points_for_card, play, get_next_card_from_deck, deal_card_to_player, player_turn, dealer_turn
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


def test_correct_draw():
    """ Tests whether the get_next_card_from_deck function correctly returns the next card """
    assert get_next_card_from_deck(["AC", "AS", "AH"]) == "AC"


def test_deck_edited():
    """ Tests whether the get_next_card_from_deck function correctly removes the next card from the deck"""
    deck = ["AC", "AS", "AH"]
    next_card = get_next_card_from_deck(deck)
    assert deck == ["AS", "AH"]


def test_hand_changed():
    """ Tests whether the deal_card_to_player function correctly changes the player's hand. """
    deck = ["AC", "AS", "AH"]
    player = {
        "hand": ["1S", "2S"],
        "name": "foo"
    }
    deal_card_to_player(deck, player)
    assert player["hand"] == ["1S", "2S", "AC"]


def test_player_bust():
    """ Tests whether the player_turn function returns False when the Player's hand 
        is already above 21. """
    deck = ["AC", "AS", "AH"]
    player = {
        "hand": ["KH", "KS", "2C"],
        "name": "John Doe"
    }
    is_player_turn = player_turn(deck, player)
    assert is_player_turn == False


def test_player_hit(capsys, monkeypatch):
    """ Tests whether the player_turn function prints "Hitting" when the user chooses to hit. """
    deck = ["AC", "AS", "AH"]
    player = {
        "hand": ["KH", "2C"],
        "name": "John Doe"
    }
    player_chooses(['hit'], monkeypatch)
    is_player_turn = player_turn(deck=deck, player=player)

    captured_output = capsys.readouterr().out

    assert "Hitting" in captured_output


def test_printed_hand(monkeypatch, capsys):
    """ Tests whether the player_turn function correctly prints the new hand after the player hits. """
    deck = ["AC", "AS", "AH"]
    player = {
        "hand": ["KH", "2C"],
        "name": "John Doe"
    }
    player_chooses(['hit'], monkeypatch)
    is_player_turn = player_turn(deck=deck, player=player)

    captured_output = capsys.readouterr().out

    assert "KH, 2C, AC" in captured_output


def test_printed_points(monkeypatch, capsys):
    """ Tests whether the player_turn function correctly prints the new point total after the player hits. """
    deck = ["AC", "AS", "AH"]
    player = {
        "hand": ["KH", "2C"],
        "name": "John Doe"
    }
    player_chooses(['hit'], monkeypatch)
    is_player_turn = player_turn(deck=deck, player=player)

    captured_output = capsys.readouterr().out

    assert "(23 points)" in captured_output


def test_player_stick(capsys, monkeypatch):
    """ Tests whether the player_turn function returns False when the Player sticks. """
    deck = ["AC", "AS", "AH"]
    player = {
        "hand": ["KH", "KS", "2C"],
        "name": "John Doe"
    }
    player_chooses(['stick'], monkeypatch)
    is_player_turn = player_turn(deck, player)
    assert is_player_turn == False


def test_player_invalid_input(capsys, monkeypatch):
    """ Tests whether the player_turn function returns False when the Player gives an invalid input. """
    deck = ["AC", "AS", "AH"]
    player = {
        "hand": ["KH", "KS", "2C"],
        "name": "John Doe"
    }
    player_chooses(['invalid'], monkeypatch)
    is_player_turn = player_turn(deck, player)
    assert is_player_turn == False


def test_printed_dealer_hand(monkeypatch, capsys):
    """ Tests whether the dealer_turn function correctly prints the new hand after the dealer hits. """
    deck = ["AC", "AS", "AH"]
    dealer_hand = ["3S", "2C"]
    player_chooses(['hit'], monkeypatch)
    dealer_hand = dealer_turn(dealer_hand, deck)

    captured_output = capsys.readouterr().out

    assert "3S, 2C, AC" in captured_output


def test_printed_dealer_points(monkeypatch, capsys):
    """ Tests whether the dealer_turn function correctly prints the new point total after the dealer hits. """
    deck = ["AC", "AS", "AH"]
    dealer_hand = ["3S", "2C"]
    player_chooses(['hit'], monkeypatch)
    dealer_hand = dealer_turn(dealer_hand, deck)

    captured_output = capsys.readouterr().out

    assert "(16 points)" in captured_output


def test_dealer_draw_message(monkeypatch, capsys):
    """ Tests whether the dealer_turn function correctly prints the draw message when the dealer hits. """
    deck = ["AC", "AS", "AH"]
    dealer_hand = ["3S", "2C"]
    player_chooses(['hit'], monkeypatch)
    dealer_hand = dealer_turn(dealer_hand, deck)

    captured_output = capsys.readouterr().out

    assert "Dealer Draws AC!" in captured_output


def test_dealer_hand(monkeypatch):
    """ Tests whether the dealer_turn function correctly updates and returns the dealer's new hand when the dealer hits. """
    deck = ["AC", "AS", "AH"]
    dealer_hand = ["3S", "2C"]
    player_chooses(['hit'], monkeypatch)
    dealer_hand = dealer_turn(dealer_hand, deck)
    assert dealer_hand == ["3S", "2C", "AC"]
