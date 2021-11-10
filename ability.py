import random

class Ability:
  def __init__(self, name, max_damage):
    self.name = name
    self.max_damage = max_damage

  def attack(self):
    minDamage = round(self.max_damage * .7)
    random_value = random.randint(minDamage, self.max_damage)
    return random_value

if __name__ == "__main__":
  ability = Ability("Debugging Ability", 75)
  print(ability.name)
  print(ability.attack()) 