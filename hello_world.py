# print("Howdy Y'all!!");

# animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan"]

# for animal in animals:
#    if len(animal) > 5:
#      print(animal)
     
# greeting = input('Pick a greeting from the following: "Hello Friend", "Hola Amigo", "Namaste":  ')

# print(greeting or 'southern')

funny_animal_name = input("List out some funny animal names: spider monkey, pig in a blanket, flying squirrel : -> ")

formatted_animal_name = funny_animal_name.split(',')


for idx, animal in enumerate(formatted_animal_name):
    if(animal):
      print(idx + 1, animal)
    
import random

fav_color = input("what is your favorite color : ->")

random_animal = random.choice(formatted_animal_name)

print("Would you like to have a", fav_color, random_animal)
