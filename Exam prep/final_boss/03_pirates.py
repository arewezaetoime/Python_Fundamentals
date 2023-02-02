def get_cities():
    command = input()
    while command != 'Sail':
        current_city = command.split('||')
        city, population, gold = current_city[0], int(current_city[1]), int(current_city[2])
        if city not in cities_dict.keys():
            cities_dict[city] = [population, gold]
        else:
            cities_dict[city][0] += population
            cities_dict[city][1] += gold
        command = input()
    return cities_dict


def plunder(current_town, current_people, current_gold):
    cities_dict[current_town][0] -= current_people
    cities_dict[current_town][1] -= current_gold
    print(f"{current_town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")
    if cities_dict[current_town][0] <= 0 or cities_dict[current_town][1] <= 0:
        del cities_dict[current_town]
        print(f"{current_town} has been wiped off the map!")


def prosper(current_town, current_gold):
    if current_gold < 0:
        return "Gold added cannot be a negative number!"
    cities_dict[current_town][1] += current_gold
    return f"{current_gold} gold added to the city treasury. {current_town} now has {cities_dict[current_town][1]} gold."


def final_result():
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for city in cities_dict.keys():
        print(f"{city} -> Population: {cities_dict[city][0]} citizens, Gold: {cities_dict[city][1]} kg")


cities_dict = {}
get_cities()

command_line = input()
while command_line != 'End':
    if 'Plunder' in command_line:
        current_line = command_line.split('=>')
        town, people, gold = current_line[1], int(current_line[2]), int(current_line[3])
        plunder(town, people, gold)

    elif 'Prosper' in command_line:
        current_line = command_line.split('=>')
        town, gold = current_line[1], int(current_line[2])
        print(prosper(town, gold))

    command_line = input()

if len(cities_dict) > 0:
    final_result()
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")