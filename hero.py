import random

class Hero:
#   default starting health is 100
    def __init__(self, name, starting_health=100):
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


# This block will only run if this script is called directly.
# prevents this block from being run when this script is imported by anotther script.
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 200)
    hero2 = Hero("Dumbledore", 20)

    hero1.fight(hero2)
