

class Card:
  def __init__(self, name, type, effect):
    self.name = name,
    self.type = type,
    self.effect = effect
  def play(self):
    pass

  def use_move(self):
    # are there moves attached to this card?
    # if so then the move is usable
    pass

  def use_effect(self):
    # use player's effect
    pass


  def Name(self):
    return self.name


