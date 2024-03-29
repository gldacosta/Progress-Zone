my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

# Python 3
my_pets

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# Python 3

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)

# Python 3

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,3)))

print(result)

# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results1 = list(zip(my_strings, my_numbers))
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results1)
print(results)

