from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        self.team_one = Team('Team 1')
        self.team_two = Team('Team 2')

    def create_ability(self):
        # Prompt for Ability information.
        # return ability with values from user Input
        name = input("What is the ability name?  ")
        max_damage = int(input(
        "What is the max damage of the ability?  "))

        return Ability(name, max_damage)

    def create_weapon(self):
        # Prompt user for Weapon information
        # return Weapon with values from user input.
        weapon_name = input("What is the weapon name?  ")
        max_damage = int(input("What is the max damage of the weapon?  "))

        return Weapon(weapon_name, max_damage)

    def create_armor(self):
        # Prompt user for Armor information
        # return Armor with values from user input.
        armor_name = input("What is the armor name?  ")
        max_block = int(input("What is the max block of the armor?  "))

        return Armor(armor_name, max_block)

    def create_hero(self):
        # Prompt user for Hero information
        # return Hero with values from user input.
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        running = True
        while running == True:
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
            elif add_item == "4":
                running = False
            else:
                print(f"{add_item} was not recognized. Please try again.")
        return hero

    def build_team_one(self):
        # Prompt the user to build team_one 
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_team_stats(self, team):
        print("\n")
        # display stats
        print(f"{team.name} Kills/Deaths statistics: {team.stats()}")
        team_kills = 0
        team_deaths = 0
        # calcualte and display average K/D
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
            kd_total = team_kills / team_deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"{team.name} average K/D was: {kd_total}")

    # print survivors
    def survivors(self, team):
        survivors = 0
        for hero in team.heroes:
            if hero.deaths == 0:
                survivors += 1
                print(f"{hero.name} from {team.name} survived the battle.")
        return survivors


    # call show stats for team one and team two
    def show_stats(self):
        self.survivors(self.team_one)
        self.survivors(self.team_two)

        self.show_team_stats(self.team_one)
        self.show_team_stats(self.team_two)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
