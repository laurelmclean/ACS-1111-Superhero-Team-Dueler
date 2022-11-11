# Import random library
import random

# important ability and armor class
from ability import Ability
from armor import Armor

class Hero:
#   default starting health is 100
    def __init__(self, name, starting_health=100):
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, opponent):
        # Stretch Goal: consider the hero's power when deciding a winner
        total_power = self.current_health + opponent.current_health
        self_chance = (self.current_health / total_power) * 100
        if (random.randint(0, 100) < self_chance):
            print(f'{self.name} defeats {opponent.name}')
        else:
            print(f'{opponent.name} defeats {self.name}')

    def add_ability(self, ability):
        #add ability objects to list.
        self.abilities.append(ability)
    
    def attack(self):
        # start total damage at 0
        total_damage = 0
         # loop through all of hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        # add armor object to list
        self.armors.append(armor)

    def defend(self):
        # run the block method on each armor in self.armors
        total_defense = 0
         # loop through all of hero's armors
        for armor in self.armors:
            # add the defense of each armor to total
            total_defense += armor.block()
        # return the total damage
        return total_defense
    
    def take_damage(self, damage):
        # Updates self.current_health to reflect the damage minus the defense.
        attack_damage = damage - self.defend()
        self.current_health -= attack_damage
        print(f"{self.name} Took {attack_damage} damage!")
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

# This block will only run if this script is called directly.
# prevents this block from being run when this script is imported by anotther script.
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 200)
    hero2 = Hero("Dumbledore", 20)

    hero1.fight(hero2)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    armor = Armor("shield", 10)
    armor2 = Armor("guard", 30)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    hero.add_armor(armor)
    hero.add_armor(armor2)
    print(hero.attack())
    print(hero.defend())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    hero.defend()
    print(hero.current_health)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
