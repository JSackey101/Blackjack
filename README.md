# Blackjack Game

## Description

One player Blackjack game which can be played in the command-line. Player draws cards and attempts to hit either 21 or a number under 21 with the hopes that the dealer will not draw an equal or higher number on their turn. If the player draws over 21 then they lose.

## Usage

To run without a defined seed use:

```
python3 blackjack.py
```

To run with a defined seed use:

```
python3 blackjack.py --seed [seed number]
```

A seed would be defined by UNIX time - the number of non-leap seconds elapsed since Jan 1 1970.

## Ruleset Used

French/German Blackjack rules.

Numbers translate directly (e.g. the 1 number cards count as 1)

Joker (J), Queen (Q), King (K) all are 10.

Ace (A) is always 11.

