from time import time
from random import Random
import argparse

LOSE_MESSAGE = "You lose!"
WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "Draw!"
SUIT_LETTERS = ["S", "D", "C", "H"]
CARD_NUMBERS = ["A", "2", "3", "4", "5",
                "6", "7", "8", "9", "10", "J", "Q", "K"]
SPECIAL_NO_DICT = {"A": 11,
                   "J": 10,
                   "Q": 10,
                   "K": 10
                   }


def shuffle(deck: list, seed: int) -> list[str]:
    """Randomises a deck of cards"""
    copy_of_deck = deck.copy()
    Random(seed).shuffle(copy_of_deck)
    return copy_of_deck


def generate_deck() -> list[str]:
    """Generates a deck of cards and returns them"""
    cards = []
    for letter in SUIT_LETTERS:
        for number in CARD_NUMBERS:
            cards.append(number+letter)

    # TODO: Write your code here to generate a deck of cards

    return cards


def points_for_card(card: str) -> int:
    """Calculates the amount of points for 1 given card"""


def points_for(cards: list[str]) -> int:
    """Calculates the amount of points for a given list of cards"""
    if len(cards) == 2:
        if cards[0][0] == "A" and cards[1][0] == "A":
            return 21
    points = 0
    for card in cards:
        if card[0:-1] in SPECIAL_NO_DICT:
            points += SPECIAL_NO_DICT[card[0:-1]]
        else:
            points += int(card[0:-1])
    if len(cards) > 5 and points < 21:
        return 21
    return points

    # TODO: Write your code here

    ...


def get_next_card_from_deck(deck: list[str]) -> str:
    """Gets the next card from the deck and returns it"""

    # TODO: Write your code here

    ...


def deal_card_to_player(deck: list[str], player: dict) -> None:
    """
    Draws a card from the deck and adds it to the player's hand
    """

    # TODO: Write your code here

    ...


def player_turn(deck: list[str], player: dict) -> bool:
    """
    Asks the player for their next choice and changes the game state
    based on their response of either 'hit' or 'stick'
    """

    print(
        f"Your hand is {', '.join(player['hand'])}({points_for(player['hand'])} points)")

    # Accept the choice from the player
    action = input('What do you want to do? ("hit" or "stick")')

    if action == "hit":

        deal_card_to_player(deck, player)

        # TODO: Implement the rest of the players turn
        # It's still the player's turn

        return True
    elif action == "stick":

        return False  # End the player's turn
    else:
        return None


def get_player_name() -> str:
    return input("What is your name?")


def play(seed: int) -> None:
    """
    Generates a deck and deals cards to the player and dealer.

    The 'seed' parameter is used to set a specific game. If you play the game
    with seed=313131 it will always have the same outcome (the order the cards are dealt)
    """
    new_deck = generate_deck()
    shuffled_deck = shuffle(new_deck, seed)
    name = get_player_name()

    print(f"Player {name} has entered the game")

    player = {
        "hand": [shuffled_deck.pop(0), shuffled_deck.pop(0)],
        "name": name
    }

    is_player_turn = True

    while is_player_turn:
        is_player_turn = player_turn(shuffled_deck, player)

        # TODO: Implement the Dealer's turn

        # TODO: Implement the end of the game


def get_seed() -> int:
    """
    You can safely ignore this function. It is used to accept a seed from the command line.
    For example

    python3 blackjack.py --seed 313131

    Would play the game with defined seed of 313131
    """
    parser = argparse.ArgumentParser("blackjack")
    parser.add_argument(
        "--seed", dest='seed', help="The seed that a game will be played with", type=int)
    args = parser.parse_args()
    seed = args.seed

    # If no seed is given, use the current time as the seed
    if seed is None:
        return time()

    return seed


if __name__ == "__main__":
    seed = get_seed()
    play(seed)
