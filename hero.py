# Import random library
import random

# important ability, armor, and weapon class
from ability import Ability
from armor import Armor
from weapon import Weapon

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

    # method to allow each hero to attack the other
    def fight(self, opponent):
        # if either hero has abilitis, they will fight
        if len(self.abilities) >= 1 or len(opponent.abilities) >= 1:
            #  while loop will continue attack as long as both are alive
            while self.is_alive() == True and opponent.is_alive() == True:
                # if hero has abilities
                if len(self.abilities) > 0:
                    total_damage = self.attack()
                    # if opponent has armor
                    if len(opponent.armors) > 0:
                        total_damage -= opponent.defend()
                        # damage they take is total minus defense
                    opponent.take_damage(total_damage)
                    # if opponent dies, print hero defeats opponent
                    if opponent.is_alive() == False:
                        print(f'{self.name} defeats {opponent.name}')
                        break
                if len(opponent.abilities) > 0:
                    total_damage = opponent.attack()
                    if len(self.armors) > 0:
                        total_damage -= self.defend()
                    self.take_damage(total_damage)
                    # if hero dies, print opponent defeats hero
                    if self.is_alive() == False:
                        print(f'{opponent.name} defeats {self.name}')
        # else, neither hero has abilities and it's a draw
        else:
            print("Draw!")


    def add_ability(self, ability):
        #add ability objects to list.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        # add weapon to abilities
        self.abilities.append(weapon)
    
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
# if __name__ == "__main__":
#     hero1 = Hero("Wonder Woman", 200)
#     hero2 = Hero("Dumbledore", 20)

#     hero1.fight(hero2)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     armor = Armor("shield", 10)
#     armor2 = Armor("guard", 30)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     hero.add_armor(armor)
#     hero.add_armor(armor2)
#     print(hero.attack())
#     print(hero.defend())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     hero.defend()
#     print(hero.current_health)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
