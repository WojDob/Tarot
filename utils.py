from random import shuffle
from time import sleep
import functools
import os
from meaning import MEANING

# Disable output buffering, animations wont work without it
print = functools.partial(print, flush=True)


def getDeck():

    # load the deck of cards from deck.txt

    try:
        deckFile = open('deck.txt')
    except IOError:
        print("Could not find the deck.")
        os.system('pause')
        exit()
    with deckFile:
        return [card.strip('\n') for card in deckFile]


def shuffleDeck(deck):

    # shuffle the cards with animated dots

    print("Shuffling cards", end='')
    for i in range(3):
        print(".", end='')
        shuffle(deck)
        sleep(1)
    print("\n")
    return deck


def draw(deck, cardNumber):

    # draw a single card from the deck

    sleep(1)
    try:
        print(deck[cardNumber])
        sleep(0.5)
        print(MEANING[deck[cardNumber]] + "\n\n")
    except KeyError:  # if someone changes the name of a card in deck.txt
        print("\nThis card is destroyed.\n\n")
    sleep(2)


def threeCardSpread(deck):

    # read fate

    print("*The past*\n")
    draw(deck, 0)
    print("*The present*\n")
    draw(deck, 1)
    print("*The future*\n")
    draw(deck, 2)


def saveDeck(deck):

    # save the shuffled deck into deck.txt

    deckFile = open('deck.txt', 'w')
    for card in deck:
        deckFile.write(card + "\n")
    deckFile.close()
