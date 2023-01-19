from time import time
from random import Random
import argparse

LOSE_MESSAGE = "You lose!"
WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "Draw!"


def shuffle(deck, seed):
    Random(seed).shuffle(deck)
    return deck


def generate_deck():
    cards = ["", "", ""]

    # TO DO: Write your code here to generate a deck of cards

    return cards


def points_for(cards):

    # TO DO: Write your code here

    return 0


def player_turn(deck, hand):
    print(f"Your hand is {', '.join(hand)}\n({points_for(hand)} points)")

    # Accept the choice from the player
    action = input('What do you want to do? ("hit" or "stick")')

    if action == "hit":

        # TO DO: Draw a card
        # It's still the player's turn

        return True
    elif action == "stick":

        #  End the player's turn

        return False
    else:
        return None


def play(seed):
    new_deck = generate_deck()
    shuffled_deck = shuffle(new_deck, seed)

    player_hand = [shuffled_deck.pop(0), shuffled_deck.pop(0)]

    is_player_turn = True

    while is_player_turn:
        is_player_turn = player_turn(shuffled_deck, player_hand)

        # TO DO: Dealer's turn


# You can safely ignore this function. It is used to accept a seed from the command line.
# For example
#   python3 blackjack.py --seed 313131
# Would play the game with defined seed of 313131
def get_seed():
    parser = argparse.ArgumentParser("blackjack")
    parser.add_argument(
        "--seed", dest='seed', help="The seed that a game will be played with", type=int)
    args = parser.parse_args()
    seed = args.seed

    if seed == None:
        return time()

    return seed


if __name__ == "__main__":
    seed = get_seed()
    play(seed)
