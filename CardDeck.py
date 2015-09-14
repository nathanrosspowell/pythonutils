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
    return list( fn(i, x) for i, n in enumerate(repeat(nums, 4)) for x in n )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Score a card.
def score(card: str, aces_high: bool = True) -> int:
    try:
        return int(card[:-1])
    except ValueError:
        pass
    score = royal.index(card[:-1])
    if aces_high == False and score == 3:
        return 1
    return score + 10
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def deal(cards, number: int = 1):
    return cards[number:], cards[:number]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Deal out cards to the table.
def deal_hands(
        players: int = 1,
        player_cards: int = 2, 
        dealer: bool = True, 
        dealer_cards_at_end: bool = False,
        cards = None):
    if cards is None:
        cards = deck()
    shuffle(cards)
    print(cards)
    hands = players
    dealer_like_player = dealer is True and dealer_cards_at_end is False
    if dealer_like_player:
        hands += 1
    players_hands = [ [] for x in range(hands) ]
    for turn in range(player_cards):
        for player in players_hands:
            cards, dealt = deal(cards, 1)
            player.append(dealt)
    if dealer:
        if dealer_like_player:
            dealer_hand = players_hands.pop()
        else:
            dealer_cards = dealer_cards_at_end if isinstance( dealer_cards_at_end, int) else player_cards
            cards, dealer_hand = deal(cards, dealer_cards)
        return cards, dealer_hand, players_hands

    else:
        return cards, players
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def cardDeckTestRun():
    print( "Starting operation.")
    cards = deck()
    print("Cards:", len(cards));
    print("~~~")
    print("Full Deck:", cards);
    print("~~~")
    shuffle(cards)
    print("Shuffled Deck:", cards)
    print("~~~")
    print("Score 5H", score("5H"))
    print("Score JD", score("JD"))
    print("Score QC", score("QC"))
    print("Score KC", score("KC"))
    print("Score AS high", score("AS"))
    print("Score AS low", score("AS", aces_high=False))
    print("~~~")
    print("BlackJack")
    cards, dealer, players = deal_hands(players = 3)
    for i, player in enumerate(players):
        print("   Player", i+1, ":", player)
    print("   Dealer:", dealer)
    print("~~~")
    print("Texas hold em")
    cards, dealer, players = deal_hands(players = 3, dealer_cards_at_end = 3)
    for i, player in enumerate(players):
        print("   Player", i+1, ":", player)
    print("   Dealer:", dealer)
    print("\nOperation done!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Direct run of the file, invoke test.
if __name__ == "__main__":
    cardDeckTestRun()
