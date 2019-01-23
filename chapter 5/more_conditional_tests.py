# more conditional tests.
name = "Hamza"
print("Is name == 'hamza'? I predict False.")
print(name == 'hamza')

print("Is name.lower() == 'hamza'? I predict True.")
print(name.lower() == 'hamza')

number = 15
print("Is number < 15? I predict False.")
print(number < 15)

print("Is number > 15? I predict False.")
print(number > 15)

number = 15
print("Is number <= 15? I predict True.")
print(number <= 15)

print("Is (number == 15) and (name == 'hamza')? I predict False.")
print((number == 15) and (name == 'hamza'))

planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
print("Is 'Pluto' in planets? I predict False.")
print('Pluto' in planets)

print("Is 'Pluto' not in planets? I predict True.")
print('Pluto' not in planets)
