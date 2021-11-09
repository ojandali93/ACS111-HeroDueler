import random

class Armor:
  def __init__(self, name, max_block):
    self.name = name
    self.max_block = max_block

  def block(self):
    randomNumber = random.randint(0, self.max_block)
    return randomNumber

if __name__ == "__main__":
  armor = Armor("Debugging Shield", 10)
  print(armor.name)
  print(armor.block())