import random
from ability import Ability

class Weapon(Ability):

    # returns a random value between one half to full attack power of weapon
    # weapon inherits max damager from ability
    def attack(self):
        weapon_value = random.randint(self.max_damage // 2, self.max_damage)
        return weapon_value
