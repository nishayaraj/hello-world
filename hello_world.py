print("Howdy Y'all!!");

animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan"]

for animal in animals:
   if len(animal) > 5:
     print(animal)
     
greeting = input('Pick a greeting from the following: "Hello Friend", "Hola Amigo", "Namaste":  ')

print(greeting or 'southern')
