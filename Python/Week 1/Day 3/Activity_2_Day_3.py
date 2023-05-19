# -take three arugments:animalSpecies, and how many litres of water the animal type drinks a day

# -This program should ask the user to type in the three values, and then a message must be printed stating the animal’s name and type, and how much water the animal type drinks.


animalType = input('Enter animal type: \n')
animalSpecies = input('Enter animal species: \n')

message_litres = f'Enter the amount of {animalType} needs to drinks a day'
print(message_litres)
litres = input('')

output = f'The {animalType}({animalSpecies}) drinks {litres}L of water a day'
print(output)
