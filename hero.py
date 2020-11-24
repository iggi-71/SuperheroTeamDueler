import random

from ability import Ability
from armor import Armor

class Hero:

    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    

    #Hint: Look into random library, more specifically the choice method

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")

    # hero1.fight(hero2)

    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)