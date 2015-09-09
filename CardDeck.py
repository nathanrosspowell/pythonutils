#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CardDeck. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from itertools import chain, repeat
from random import shuffle
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def deck():
    nums = list(chain(range(1,11), "JQKQ"));
    fn = lambda i, x: "CSHS"[i] + str(x)
    return [ fn(i, x) for i, n in enumerate(repeat(nums, 4)) for x in n ]
# Test run.
def cardDeckTestRun():
    print( "Starting operation.")
    print("Full Deck:", list(deck()))
    print("~~~")
    to_shuffle = list(deck())
    shuffle(to_shuffle)
    print("Shuffled Deck:", to_shuffle)
    print("\nOperation done!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Direct run of the file, invoke test.
if __name__ == "__main__":
    cardDeckTestRun()
