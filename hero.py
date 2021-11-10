import random
from ability import Ability
from armor import Armor

class Hero:
  def __init__(self, name, starting_health):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.abilities = list()
    self.armors = list()
  
  def fight(self, opponent):
    while opponent.is_alive() == True and self.is_alive() == True:
      self.take_damage(opponent.attack())
      opponent.take_damage(self.attack())
      if opponent.is_alive() == False:
          print(f"{self.name} has won! ")
          return self.name
      if self.is_alive() == False:
          print(f"{opponent.name} has won! ")
          return opponent.name
  
  def add_ability(self, ability):
    self.abilities.append(ability)

  def add_armor(self, armor):
    self.armors.append(armor)
  
  def defend(self):
    total_armor = 0
    for armor in self.armors:
      total_armor += armor.block()
    return total_armor

  def attack(self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.block()
    return total_damage
  
  def take_damage(self, damage):
    total_armor = self.defend()
    if total_armor >= damage:
      return self.current_health 
    if total_armor < damage:
      remaining_damage = damage - total_armor
      self.current_health = self.starting_health - remaining_damage
      return self.current_health

  def is_alive(self):
    if self.current_health <= 0:
      return False
    else:
      return True

if __name__ == "__main__":
  hero = Hero("Grace Hopper", 200)
  hero.take_damage(150)
  print(hero.is_alive())
  hero.take_damage(15000)
  print(hero.is_alive())