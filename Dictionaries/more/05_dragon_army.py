def input_validation(n_val, type_val, name_val, dmg_val, health_val, armor_val):
    if n_val in range(0, 100):
        if type_val[0].isalpha and name_val[0].isalpha:
            if dmg_val in range(0, 100_000) or dmg_val == 'null' and\
                health_val in range(0, 100_000) or health_val == 'null' and\
                    armor_val in range(0, 100_000) or armor_val == 'null':
                return True
    return False


def get_averages(colour):
    average_dmg = []
    average_health = []
    average_armor = []
    for dmg in dict_dragons[colour].items():
        average_dmg.append(dmg[1][damage_key])
    for hp in dict_dragons[colour].items():
        average_health.append(hp[1][health_key])
    for arm in dict_dragons[colour].items():
        average_armor.append(arm[1][armor_key])
    if len(average_dmg) != 0 and len(average_health) != 0 and len(average_armor) != 0:
        average_values = [(sum(average_dmg) / len(average_dmg)), (sum(average_health) / len(average_health)),
                          (sum(average_armor) / len(average_armor))]
        return average_values


def add_dragons(type_d, name, dmg, hp, armor):
    if type_d not in dict_dragons.keys():
        dict_dragons[type_d] = {}
    if name not in dict_dragons[type_d]:
        dict_dragons[type_d][name] = {damage_key: dmg, health_key: hp, armor_key: armor}
    else:
        dict_dragons[type_d][name] = {damage_key: dmg, health_key: hp, armor_key: armor}


def get_dragons(n):
    for _ in range(n):
        dragon_input = input().split()
        type_dragon = ''
        name_dragon = ''
        damage_dragon = 0
        health_dragon = 0
        armor_dragon = 0
        default_values = {'hp': 250, 'dmg': 45, 'armor': 10}
        if len(dragon_input) == 5:
            if 'null' not in dragon_input:
                type_dragon, name_dragon, damage_dragon, health_dragon, armor_dragon = \
                    dragon_input[0], dragon_input[1], dragon_input[2], dragon_input[3], dragon_input[4]
                # Validating the data and then passing it to ADD function
                if input_validation(n_times, str(type_dragon), str(name_dragon), int(damage_dragon), int(health_dragon),
                                    int(armor_dragon)):
                    add_dragons(str(type_dragon), str(name_dragon), int(damage_dragon), int(health_dragon), int(armor_dragon))
            else:
                index_of_null = dragon_input.index('null')
                type_dragon, name_dragon, damage_dragon, health_dragon, armor_dragon = dragon_input[0], \
                                                                                        dragon_input[1], \
                                                                                        dragon_input[2], \
                                                                                        dragon_input[3], \
                                                                                        dragon_input[4]
                if index_of_null == 2:
                    damage_dragon = default_values['dmg']
                elif index_of_null == 3:
                    health_dragon = default_values['hp']
                elif index_of_null == 4:
                    armor_dragon = default_values['armor']
                # Validating the data and then passing it to ADD function
                if input_validation(n_times, str(type_dragon), str(name_dragon), int(damage_dragon), int(health_dragon), int(armor_dragon)):
                    add_dragons(str(type_dragon), str(name_dragon), int(damage_dragon), int(health_dragon), int(armor_dragon))


# type_key = 'Type'
# name_key = 'Name'
damage_key = 'Damage'
health_key = 'Health'
armor_key = 'Armor'

dict_dragons = {}
n_times = int(input())
get_dragons(n_times)

for color in dict_dragons.keys():
    averages = get_averages(color)
    if averages:
        print(f"{color}::({averages[0]:.2f}/{averages[1]:.2f}/{averages[2]:.2f})")
    for name in sorted(dict_dragons[color].items()):
        print(f"-{name[0]} -> damage: {name[1][damage_key]}, health: {name[1][health_key]}, armor: {name[1][armor_key]}")

'name'.isidentifier()
