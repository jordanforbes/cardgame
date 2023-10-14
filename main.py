

class Card:
  def __init__(self, hp: int,name: str, cost:int, ability:str, move_slots:list):
    self.name = name,
    self.hp = hp,
    self.cost = cost,
    self.ability = ability,
    self.move_slots = move_slots,
    self.art = '';
    self.moves = []

  def play(self):
    pass

  def use_move(self):
    # are there moves attached to this card?
    # if so then the move is usable
    pass

  def use_effect(self):
    # use player's effect
    pass

  def die(self):
    # send card to grave
    pass

# moves are attatched to Cards if the card has the right amount of slots
class Move:
  def __init__(self, name:str, type:str, effect:str, slots:int):
    self.name = name,
    self.type = type, #is it attack or effect?
    self.effect = effect,
    self.slots = slots #how many slots does it take up

  # attach move to card
  def attach(self, card: Card):
    # does card have the right number of move_slots?
      # if so then the move can be attached
    pass

class Deck:
  # contains all cards in player's deck
  pass

class Player:
  def __init__(self, deck:Deck):
    self.hp = 20,
    self.energy = 4
    self.deck = deck
    self.hand = []

  def add_to_hand(self):
    # are there cards in deck? add them to your hand
    pass

  def use_card(self):
    # do you have enough energy?
    # subtract cost from player's energy
    # play card
    pass

