class Card:
  def __init__(self, name: str, cost:int, ability:str, move_slots:list):
    self.name = name,
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
