import random

class Team:
    def __init__(self, name):
        # team name and empty list of heroes
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
    # remove hero from list or return 0 if hero not found
        foundHero = False
        # loop through each hero in list
        for hero in self.heroes:
            # if found, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set indicator to True
                foundHero = True
        # if we did not find hero,return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        # Prints out all heroes to the console.
        for hero in self.heroes:
            print(f"Hero name: {hero.name}.")

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        # Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
    
    def revive_heroes(self, health=100):
        # Reset all heroes health to starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} health has been revived!")

    def attack(self, other_team):
        # Battle each team against each other.

        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)
            hero1.fight(hero2)
            if hero1.is_alive() == False:
                living_heroes.remove(hero1)
            if hero2.is_alive() == False:
                living_opponents.remove(hero2)

