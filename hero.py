import random

from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armor = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self):
        self.blocked_damage = 0
        for armor in self.armor:
            self.blocked_damage -= armor.block()
        return self.blocked_damage

    def take_damage(self, damage):
        if abs(self.blocked_damage) < damage:
            rec_damage = damage + self.blocked_damage
            self.current_health -= rec_damage
            print(f"This is damage received: {rec_damage}")
        elif abs(self.blocked_damage) >= damage:
            rec_damage = 0
        return self.current_health



    def is_alive(self):
        if self.current_health > 0:
            return True
        elif self.current_health <= 0:
            return False

    def fight(self, opponent):
        fighters = [self, opponent]
        if not self.abilities or not opponent.abilities:
            print("Evenly Matched!")
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                print("Keep fighting!")




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)