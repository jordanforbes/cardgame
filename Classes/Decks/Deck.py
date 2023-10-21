import sys
from ..Cards.Card import Card
import random
class Deck:
  def __init__(self):
  # contains cards
    self.cards = []
  # adds to deck

  def addCard(self, card, location):
    if(location == "top"):
      self.cards.insert(0, card)

    if(location == "bottom"):
      self.cards.insert(len(self.cards), card)

    if(location == "random"):
      rand = random.randint(0, len(self.cards))
      print(f"random number: {rand}")
      self.cards.insert(rand, card)


  # removes from deck
  def drawCard(self):
    drawnCard = self.cards[0]
    self.cards.pop(0)
    return drawnCard

  # shuffles deck
  def shuffle(self):
    print("shuffling...")
    random.shuffle(self.cards)

  # Show cards
  def showCards(self):
    for card in self.cards:
      print(f"{card.name}")

  def drawCertainCard(self):
    pass

  def removeCartainCard(self):
    pass

  def sendToGrave(self):
    pass

  def playCard(self):
    pass

# pCards=["Ace of Spades","King of Clubs", "Queen of Hearts","Jack of Diamonds", "10 of Spades"]

# examples of decks:
# draw deck
# hand
# items
# grave
# c1 = Card("Ace", "a type here", "an effect")
# c2 = Card("King", "a type here", "an effect")
# c3 = Card("Queen", "a type here", "an effect")
# c4 = Card("Jack", "a type here", "an effect")
# c5 = Card("10", "a type here", "an effect")

# pCards=[c1, c2, c3, c4, c5]

# testDeck = Deck()
# testDeck.addCard(pCards[0],'top')
# testDeck.addCard(pCards[1], 'top')
# testDeck.addCard(pCards[2],"top")
# testDeck.addCard(pCards[3],"top")
# testDeck.addCard(pCards[4],"random")
# print("cards added")
# testDeck.showCards()
# testDeck.shuffle()
# testDeck.showCards()
# print(" ")
# print("drawing a card")
# print(testDeck.drawCard().name)
# print("rest of deck")
# testDeck.showCards()

# 0 c1 = Card("Ace", "a type here", "an effect")
# 1 c2 = Card("King", "a type here", "an effect")
# 2 c3 = Card("Queen", "a type here", "an effect")
# 3 c4 = Card("Jack", "a type here", "an effect")
# 4 c5 = Card("10", "a type here", "an effect")
