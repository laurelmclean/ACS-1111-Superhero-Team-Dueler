# inheritance example 

# animal class
class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating")

  def drink(self):
    print(f"{self.name} is drinking")

# frog as subclass of animal
class Frog(Animal):
    def jump(self):
      print(f"{self.name} is jumping")


dog = Animal("Sophie")
dog.eat()
dog.drink()

frog = Frog("Ribby")
frog.eat()
frog.drink()
frog.jump()
