from random import shuffle
from time import sleep
import functools
import os

#Disable output buffering, animations wont work without it
print = functools.partial(print, flush=True)

def getDeck():

	#load the deck of cards from deck.txt

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
	sleep(2)

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

#Dictionary with meanings of different cards

meaning = {
	"The Fool":"Immaturity, sincerity, the natural man, a free spirit. One who naturally knows his will and is worry free. A dreamer, careless and disinterested in practical matters. Travel.",
	"The Magician":"Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where he is going and how to achieve its ends.",
	"The High Priestess":"Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition, possibly given by a woman. Psychic ability. The manifestation of the eternal feminine in a spiritual way.",
	"The Empress":"Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development.",
	"The Emperor":"Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person.",
	"The Hierophant":"Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart. The card that represents you, in the form of your own, truest voice, your own inner-self.",
	"The Lovers":"Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life.",
	"The Chariot":"Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel.",
	"Justice":"Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. In order to keep things balanced certain things must be sacrificed.",
	"The Hermit":"Pilgrimage. Quest for wisdom. A period of spiritual and intellectual personal development. ",
	"The Wheel of Fortune":"Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions.",
	"Strength":"Sublimation or regulation of the passions and lower instincts. Success. Powerful will and great physical strength. The inner strength to tame the lust.",
	"The Hanged Man":"Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation.",
	"Death":"Complete transformation. Death and rebirth. The end of something. Evolution from one state to another.",
	"Temperance":"Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint.",
	"The Devil":"Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out. ",
	"The Tower":"Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. \"Finger of God\". Bankruptcy. Sudden death.",
	"The Star":"Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health. ",
	"The Moon":"Intuition, threshold of an important change, arduous and obscure path, development of psychic powers. ",
	"The Sun":"Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others. ",
	"Judgement":"Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment.",
	"The World":"Success granted. Rewards. Travel, emigration, change of residence.",
	"Ace of Wands":"Creation, birth. The power or ability to begin or to follow through energetically with a plan or task; enterprise and determination.",
	"Two of Wands":"Dominion. Maturity. Boldness with self-control. Influence. ",
	"Three of Wands":"Virtue. Established strength, realization of hope, nobility. Cooperation, partnership. ",
	"Four of Wands":"Completion. Settlement, peace, harmony. Romance, marriage, society.",
	"Five of Wands":"Strife. Competition, lawsuit, obstacles, violence, fighting. ",
	"Six of Wands":"Victory after strife. Good news. Progress, helping friends. ",
	"Seven of Wands":"Valor. Victory through courage. Struggle. Fierce competition. Certain success.",
	"Eight of Wands":"Swiftness. Hasty decision. Air travel, messages. Love letter. Hyperactivity. Great hopes. ",
	"Nine of Wands":"Strength. Capability of enduring a long struggle and achieve the final victory. Recovery from sickness.",
	"Ten of Wands":"Oppression. Imbalance and selfishness. Heavy burden. Force detached from spiritual sources. A problem may be solved soon. ",
	"Page of Wands":"Young and brilliant. Enthusiastic and daring. A messenger or bearer of tidings. ",
	"Knight of Wands":"A young and energetic man. Swift and daring. May be noble and generous but also violent and hasty. ",
	"Queen of Wands":"Kind, energetic but calm woman. Conservative, pragmatic and authoritarian. Fruitful in mind and body. ",
	"King of Wands":"Courageous, swift and generous man. Passionate and strong. Paternalistic and proud. Unexpected heritage; a good marriage. ",
	"Ace of Cups":"Harmony, fertility, happiness, beginning of great love. ",
	"Two of Cups":"Love. Harmony, warm friendship. Close relation with a kindred soul. Good for business and love. ",
	"Three of Cups":"Abundance. Pleasure, hospitality, success. The good things of life. ",
	"Four of Cups":"Luxury. Abandonment to desire. New ambition. ",
	"Five of Cups":"Disappointment. Unexpected misfortune. Partial loss. Friendship or love gone. Inheritance. ",
	"Six of Cups":"Pleasure. Happiness coming from the past. Nostalgia. Success. ",
	"Seven of Cups":"Debauch. Foolish expectations. Illusory dreams, deceit. Intoxication. Drug addiction. ",
	"Eight of Cups":"Indolence. Instability. Material success abandoned, may be for something higher. Decline in interest. Wandering. ",
	"Nine of Cups":"Happiness. Complete material success and well-being. You will get what you wish. ",
	"Ten of Cups":"Satiety. Perfect love and lasting contentment. Peace, friendship. ",
	"Page of Cups":"Quiet and studious youth, but also sweet and dreamy. News or proposition. ",
	"Knight of Cups":"A young man may be an artist, who is graceful and poetic. He is an indolent dreamer of sensual pleasures. Can mean a messenger, a proposition or an invitation. ",
	"Queen of Cups":"Dreamy, calm, poetic, imaginative, kind yet not willing to take much trouble for another. ",
	"King of Cups":"A man skilled in law or trade and interested in science, art, religion or philosophy. A good friend, liberal, idealistic and creative. Kind and willing to take some responsibility. ",
	"Ace of Swords":"Conquest. Triumph through trouble. Intense activity. Gestation or parturition. ",
	"Two of Swords":"Peace. Balanced forces. Indecision. Strength. Friendship. ",
	"Three of Swords":"Sorrow. Separation, quarrel, tears. Delay. Absence. ",
	"Four of Swords":"Truce. Solitude. Stagnation. Recovering from illness. Exile. Retreat. ",
	"Five of Swords":"Defeat. Failure. Loss. Powerlessness. Separation. Lies. Death. ",
	"Six of Swords":"Science. Journey by water, revelation, study. Intelligent effort. Success after anxiety. ",
	"Seven of Swords":"Futility. Partial or unpredictable result. Dreams, vacillation. Travel by land. ",
	"Eight of Swords":"Interference. Restriction. Temporal sickness or captivity. Indecision. ",
	"Nine of Swords":"Cruelty. Suffering. Misery. Sickness. Martyrdom. Burden. May be death of a loved one. ",
	"Ten of Swords":"Ruin. Total defeat. Death. The end of an illusion. ",
	"Page of Swords":"Logic and penetrating young man or woman. Mentally and physically dexterous. Spying. Messages.",
	"Knight of Swords":"Audacious, clever and gallant; spirited young man. He may be domineering and unstable but he has the better intentions. ",
	"Queen of Swords":"A graceful but stern woman. She has keen insight and good judgment. May be a dancer, a widow or a childless woman. This card also means privation and mourning.",
	"King of Swords":"This man may be a very good ally or counselor. He is clever and self-controlled and has some authority. Also is modern, analytical and very strong. The card may also mean a lawsuit. ",
	"Ace of Pentacles":"The beginning of prosperity and wealth. Pleasure and beauty. ",
	"Two of Pentacles":"Change. Alternation of gain and loss. Equilibrium in the midst of change. Ability to adapt to new circumstances. Some complications. Unstable mood. ",
	"Three of Pentacles":"Works. Task well done. Commercial transactions. Professional growth. Dignity. A male child. ",
	"Four of Pentacles":"Purely material gain and security. A gift or an inheritance. A female child. Greed. ",
	"Five of Pentacles":"Worry. Loss of money or employment. Poverty. Defeat. Lovers. Sympathy found in the midst of trouble. ",
	"Six of Pentacles":"Success. Material gain and power. Sharing with others the wealth. ",
	"Seven of Pentacles":"Failure. Defeat. Loss of money. Hard work but little gain. Greedy. ",
	"Eight of Pentacles":"The first steps of a profitable profession. Learning a business or profession. Ability in material affairs. A brunette. ",
	"Nine of Pentacles":"Gain. Practical wisdom limited to everyday affairs and the home. Stability. Solitude. Inheritance. ",
	"Ten of Pentacles":"Wealth. Fulfillment of material fortune. Family matters. Inheritance. House. ",
	"Page of Pentacles":"A learned young person, careful and reflective. Good management, kind and benevolent. The bearer of good news and messages. ",
	"Knight of Pentacles":"Mature and responsible, a trustworthy and laborious man. A capable manager. An important matter concerning money. ",
	"Queen of Pentacles":"Charming and generous woman. Pragmatic and quiet, but ambitious. Opulence, security. ",
	"King of Pentacles":"A married man, wealthy and clever in money matters. Patient and laborious, he is an experimented chief and a reliable ally. ",
}

