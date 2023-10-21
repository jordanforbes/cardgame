from Cards.Card import Card
import random

pCards=["Ace of Spades","King of Clubs", "Queen of Hearts","Jack of Diamonds", "10 of Spades"]

# examples of decks:
# draw deck
# hand
# items
# grave

class Deck:
  def __init__(self):
    self.cards = []
  # contains cards
  def addCard(self, card):
    self.cards.append(card)
  # adds to deck
  def RemoveCard(self):
    self.cards.pop(0)
    self
  # removes from deck
  # shuffles deck

  pass


testDeck = Deck()
print(pCards)
print(testDeck.cards)
testDeck.addCard(pCards[0])
testDeck.addCard(pCards[1])
testDeck.addCard(pCards[2])
testDeck.addCard(pCards[3])
testDeck.addCard(pCards[4])
print(testDeck.cards)
testDeck.RemoveCard()
print(testDeck.cards)
