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
    


