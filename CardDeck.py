#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CardDeck. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from itertools import chain, repeat
from random import shuffle
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Globals
suits = "CDHS"
royal = "JQKA" # score built into the order.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Make a deck.
def deck():
    nums = list(chain(range(2,11), royal));
    fn = lambda i, x: str(x) + suits[i]
    return [ fn(i, x) for i, n in enumerate(repeat(nums, 4)) for x in n ]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# score
def score(card, aces_high = True):
    try:
        return int(card[:-1])
    except ValueError:
        pass
    score = royal.index(card[:-1])
    if aces_high == False and score == 3:
        return 1
    return score + 10
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def cardDeckTestRun():
    print( "Starting operation.")
    cards = list(deck())
    print("Cards:", len(cards));
    print("~~~")
    print("Full Deck:", cards);
    print("~~~")
    to_shuffle = list(deck())
    shuffle(to_shuffle)
    print("Shuffled Deck:", to_shuffle)
    print("~~~")
    print("Score 5H", score("5H"))
    print("Score JD", score("JD"))
    print("Score QC", score("QC"))
    print("Score KC", score("KC"))
    print("Score AS high", score("AS"))
    print("Score AS low", score("AS", False))
    print("\nOperation done!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Direct run of the file, invoke test.
if __name__ == "__main__":
    cardDeckTestRun()
