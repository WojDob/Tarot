from random import shuffle
from time import sleep
from meaning import meaning
import os
import functools

	
"""Script to understand your fate"""
	


#Disable output buffering, animations dont work witout it
print = functools.partial(print, flush=True)

def getDeck():

	#Load the deck of cards from deck.txt

	try:
		deckFile = open('deck.txt')
	except IOError:
		print ("Could not find the deck.")
		os.system('pause')
		exit()
	with deckFile:
		return [card.strip('\n') for card in deckFile]

def shuffling(deck):

	#shuffle the cards with animated dots

	print("Shuffling cards", end = '')
	for i in range(3):
		print(".", end = '')
		shuffle(deck)
		sleep(1)
	print("\n")
	return deck

def draw(deck,cardNumber):

	#draw a single card from the deck

	sleep(1)
	try:
		print(deck[cardNumber])
		sleep(0.5)
		print(meaning[deck[cardNumber]] + "\n\n")
	except KeyError: #if someone changes the name of a card in deck.txt
		print("\nThis card is destroyed.\n\n")
	sleep(1)

def threeCardSpread(deck):

	#Read fate

	print("*The past*\n")
	draw(deck, 0)
	print("*The present*\n")
	draw(deck, 1)
	print("*The future*\n")
	draw(deck, 2)

def saveDeck(deck):

	#Save the shuffled deck into deck.txt

	deckFile = open('deck.txt', 'w')
	for card in deck:
		deckFile.write(card+ "\n")
	deckFile.close()




if __name__ == '__main__':
	answer = input("Would you like to know your fate?\n")

	if answer.lower() in ["yes", "yes please", "of course", "why not?", "sure", "yea", "yeah", "yup", "yep", "y"]:
		deck = getDeck()
		deck = shuffling(deck)
		threeCardSpread(deck)
		saveDeck(deck)
		os.system('pause')
	exit()	