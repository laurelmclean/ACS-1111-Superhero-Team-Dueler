# Import random library
import random

# important ability, armor, and weapon class
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

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
        # kills and deaths default starting value is zero
        self.deaths = 0
        self.kills = 0

    # method to allow each hero to attack the other
    def fight(self, opponent):
        # if neither hero has abilities and it's a draw
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print('Draw!')
            return
        # else either hero has abilitis, they will fight
        else:
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
                        self.add_kill(1)
                        opponent.add_death(1)
                        break
                if len(opponent.abilities) > 0:
                    total_damage = opponent.attack()
                    if len(self.armors) > 0:
                        total_damage -= self.defend()
                    self.take_damage(total_damage)
                    # if hero dies, print opponent defeats hero
                    if self.is_alive() == False:
                        print(f'{opponent.name} defeats {self.name}')
                        opponent.add_kill(1)
                        self.add_death(1)
        


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
    
    def add_kill(self, num_kills):
        # Update self.kills by num_kills amount
        self.kills += num_kills

    def add_death(self, num_deaths):
        # Update deaths with num_deaths
        self.deaths += num_deaths
