class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("dog initialized!")

  def bark(self):
    print("Woof!")

my_dog = Dog("Zues", "German Shepard")
my_dog.bark()