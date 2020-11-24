class Animal:
    def __init__(self, name, eat, drink):
        self.name = name
        self.eat = eat
        self.drink = drink

    def eating(self):
        print(f'{self.name} is eating {self.eat}')

    def drinking(self):
        print(f'{self.name} is drinking {self.eat}')

class Frog(Animal):
    def jump(self):
        print(f'{self.name} is jumping')


my_pet = Animal("Snow", "carrots", "water")
my_pet.drinking()
my_pet.eating()

hop = Frog("Hop", "lettuce", "soda")
hop.eating()
hop.jump()