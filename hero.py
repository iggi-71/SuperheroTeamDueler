import random

from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name

        self.abilities = list()
        self.armors = list()

        self.starting_health = starting_health
        self.current_health = starting_health

        self.kills = 0
        self.deaths = 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def add_ability(self, ability):
        self.abilities.append(ability)
        
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage):
        # defend_amt = 0

        for armor in self.armors:
            damage -= armor.defend()
        return damage

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        # return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive() == True:
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} wins!")
            elif opponent.is_alive() == True:
                opponent.add_kill(1)
                self.add_death(1)
                print(f"{opponent.name} wins!")


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())