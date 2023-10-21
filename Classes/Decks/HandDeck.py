from ..Decks.Deck import Deck
from ..Cards.Card import Card


class HandDeck(Deck):
  def __init__(self, deck):
    super().__init__()
    self.deck = deck

  def drawCard(self):
    drawn = self.deck.drawCard()
    self.cards.append(drawn)


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
# testDeck.addCard(pCards[4],"top")
# print("test Deck")
# print(testDeck.showCards())


# testHand = HandDeck(testDeck)
# print('test')
# print(testHand.showCards())
# testHand.drawCard()
# print('draw card')
# print(testDeck.showCards())
# print(testHand.showCards())
# testHand.drawCard()
# print('draw card')
# print(testDeck.showCards())
# print(testHand.showCards())
