import utils
import os

	
"""Console application to understand your fate"""

if __name__ == '__main__':
	answer = input("Would you like to know your fate?\n")

	if answer.lower() in ["yes", "yes please", "of course", "why not?", "sure", "yea", "yeah", "yup", "yep", "y"]:
		deck = utils.getDeck()
		deck = utils.shuffling(deck)
		utils.threeCardSpread(deck)
		utils.saveDeck(deck)
	exit()	