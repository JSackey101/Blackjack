""" Contains a function needed for testing. """

def player_chooses(choices: list, monkeypatch) -> None:
    """
    Take a list of choices and uses them to feed into the game to test with

    For example, if this is run with ["hit", "stick"] then in the game the player will
    first choose hit and then choose stick.

    Monkeypatch is used to fake (or 'mock') the input from the user
    """
    answers = iter(choices)
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
