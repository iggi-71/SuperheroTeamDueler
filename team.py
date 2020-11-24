import random
from hero import Hero

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
    # loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
            foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                print(f'{hero.name} Kill/Deaths:0')
            else:
                kd = hero.kills / hero.deaths
                print(f'{hero.name} Kill/Deaths:{kd}')

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

            for hero in other_team.heroes:
                living_opponents.append(hero)

            while len(living_heroes) > 0 and len(living_opponents) > 0:
                hero_fighter = random.choice(living_heroes)
                opponent_fighter = random.choice(living_opponents)
                hero_fighter.fight(opponent_fighter)

                if hero_fighter.is_alive() == True:
                    living_opponents.remove(opponent_fighter)
                elif opponent_fighter.is_alive() == True:
                    living_heroes.remove(hero_fighter)

                return (living_heroes, living_opponents)