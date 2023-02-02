n = int(input())
plant_dict = {}
for _ in range(n):
    current_plant = input().split('<->')
    plant, rarity = current_plant[0], current_plant[1]
    plant_dict[plant] = {}
    plant_dict[plant]['rarity'] = rarity
    plant_dict[plant]['ratings'] = []

command = input()
while command != 'Exhibition':
    command = command.split(': ')
    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        plant_dict[plant]['ratings'].append(int(rating))
    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        plant_dict[plant]['rarity'] = new_rarity
    elif command[0] == 'Reset':
        plant = command[1]
        plant_dict[plant]['ratings'] = 0
    command = input()
print("Plants for the exhibition:")
for key, values in plant_dict.items():
    rarity = values['rarity']
    rating = values['ratings']
    if rating != 0:
        average = sum(plant_dict[key]['ratings']) / len(plant_dict[key]['ratings'])
    else:
        average = rating
    print(f"- {key}; Rarity: {rarity}; Rating: {average:.2f}")



# print(plant_dict)
# print(plant_dict.keys())
# print(plant_dict.values())
# print(plant_dict['Arnoldii'].keys())
# print(plant_dict['Arnoldii'].values())



# print(plant_dict)
# plant_dict['Arnoldii']['ratings'] = []
# plant_dict['Arnoldii']['ratings'].append('5')
# plant_dict['Arnoldii']['ratings'].append('5')
# print(f"{' '.join(plant_dict['Arnoldii']['ratings'])}")
