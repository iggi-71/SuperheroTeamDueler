import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        half_max_damage = self.max_damage // 2
        weapon_damage = (random.randint(half_max_damage, self.max_damage))
        return weapon_damage