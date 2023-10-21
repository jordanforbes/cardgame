
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

# contains all cards in player's deck



print("Welcome to game")
