
dict_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
materials = input().split()
obtained = False
while not obtained:

    for index in range(0, len(materials), 2):
        quantity = materials[index]
        material = materials[index + 1].lower()

        if material not in dict_materials.keys():
            dict_materials[material] = 0
        dict_materials[material] += int(quantity)

        if dict_materials['shards'] >= 250:
            obtained = True
            print("Shadowmourne obtained!")
            dict_materials['shards'] -= 250
        if dict_materials['fragments'] >= 250:
            obtained = True
            print("Valanyr obtained!")
            dict_materials['fragments'] -= 250
        if dict_materials['motes'] >= 250:
            obtained = True
            print('Dragonwrath obtained!')
            dict_materials['motes'] -= 250
        if obtained:
            break
    if obtained:
        break
    materials = input().split()

for item, left in dict_materials.items():
    print(f"{item}: {left}")
