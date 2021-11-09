import random

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
  
  def fight(self, opponent):
    print(opponent)
    winnerCount = random.randint(0, 1)
    if winnerCount < .49:
      print(f'{self.name} has defeated {opponent.name}!')
    if winnerCount >= .49:
      print(f'{opponent.name} has defeated {self.name}!')

if __name__ == "__main__":
  ironMan = Hero('Iron Man', 200)
  hulk = Hero("hulk", 450)
  ultron = Hero("Ultron", 500)

  ironMan.fight(hulk)