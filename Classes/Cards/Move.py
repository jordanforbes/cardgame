from Card import Card

class Move(Card):
  def __init__(self, name:str, type:str, effect:str, slots:int):
    super().__init__(name, type, effect)
    self.slots = slots #how many slots does it take up

  # attach move to card
  def attach(self, card: Card):
    # does card have the right number of move_slots?
      # if so then the move can be attached
    pass
