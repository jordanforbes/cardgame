from Card import Card

class MonsterCard(Card):
  def __init__(self,name, type, effect, hp):
    super().__init__(name, type, effect)
    self.hp = hp
    self.alive = True

  def isAlive(self):
    if(self.hp <= 0):
      self.alive = False
      print(f"{self.Name()} has died")
    pass

  def loseHP(self, dmg):
    self.hp -=dmg
    self.isAlive()

mon = MonsterCard("guy", "a type here", "an effect", 8)

print(mon.Name())
print(mon.hp)
print(mon.type)
print(mon.effect)
mon.loseHP(2)
print(mon.hp)
mon.loseHP(6)
print(mon.hp)
mon.loseHP(-5)
print(mon.hp)
