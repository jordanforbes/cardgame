from .Cards.Card import Card
from .Decks.Deck import Deck
from .Decks.HandDeck import HandDeck

class Player:
  def __init__(self, deck, hand):
    self.hp = 20
    self.energy = 4
    self.deck = deck
    self.hand = hand
    self.turn = True

  def add_hp(self):
    pass

  def lose_hp(self):
    pass

  def use_card(self):
    # do you have enough energy?
    # subtract cost from player's energy
    # play card
    pass

  def end_turn(self):
    # if player chooses to end turn, turn ends
    pass

  def lose(self):
    # if hp = 0 then player loses
    print("you lose")
    pass


c1 = Card("Ace", "a type here", "an effect")
c2 = Card("King", "a type here", "an effect")
c3 = Card("Queen", "a type here", "an effect")
c4 = Card("Jack", "a type here", "an effect")
c5 = Card("10", "a type here", "an effect")
pCards=[c1, c2, c3, c4, c5]
testDeck = Deck()
testDeck.addCard(pCards[0],'top')
testDeck.addCard(pCards[1], 'top')
testDeck.addCard(pCards[2],"top")
testDeck.addCard(pCards[3],"top")
testDeck.addCard(pCards[4],"top")


testHand = HandDeck(testDeck)
testHand.drawCard()
testHand.drawCard()

p1 = Player(testDeck, testHand)
print(p1.hp)
print(p1.energy)
print(p1.deck.showCards())
print(p1.hand.showCards())
