class Player:
  def __init__(self, deck:Deck):
    self.hp = 20,
    self.energy = 4
    self.deck = deck
    self.hand = []

  def add_hp(self):
    pass

  def lose_hp(self):
    pass

  def add_to_hand(self):
    # are there cards in deck? add them to your hand
    # remove card from deck
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
    pass
