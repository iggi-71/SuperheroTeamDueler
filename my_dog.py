# my_dogs.py
import dog # we need to specify exactly what we want

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

first_dog = dog.Dog("Garfield", "Beagle")
second_dog = dog.Dog("Snoop Dog", "Bulldog")
third_dog = dog.Dog("Dogzilla", "Poodle")
print(first_dog.name, second_dog.breed)
print(second_dog.name, second_dog.breed)
print(third_dog.name, second_dog.breed)

print(first_dog.bark())
print(second_dog.roll())
print(third_dog.name, third_dog.sit())