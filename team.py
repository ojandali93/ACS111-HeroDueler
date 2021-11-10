import random

class Team:
  def __init__(self, name):
    self.name = name
    self.heroes = list()

  def remove_hero(self, name):
    foundHero = False
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        foundHero = True
    if not foundHero:
      return 0
  
  def view_all_heroes(self):
    for item in self.heroes:
      print(item)

  def add_hero(self, hero):
    self.heroes.append(hero)
  
  def stats(self):
    for hero in self.heroes:
      kd = hero.kills / hero.deaths
      print("{} Kill/Deaths:{}".format(hero.name,kd))

  def revive_heroes(self, health=100):
    for hero in self.heroes: 
      self.current_health = self.starting_health

  def attack(self, other_team):

    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents)> 0:
      living = random.choice(living_heroes)
      self.name.fight(self.name)
      living_heroes.append(self.name)
      living_opponents.append(self.name)