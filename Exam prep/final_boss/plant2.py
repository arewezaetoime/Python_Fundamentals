def check_plant(check):
    if check in plant_dict:
        return True
    print('error')


def rate_command(rate):
    rate = rate.split(' - ')
    plant_name, plant_rating = rate[0], int(rate[1])
    if check_plant(plant_name):
        plant_dict[plant_name][1].append(plant_rating)


def update_command(upd_command):
    upd_command = upd_command.split(' - ')
    plant_name, new_rarity = upd_command[0], int(upd_command[1])
    if check_plant(plant_name):
        plant_dict[plant_name][0] = new_rarity


def reset_command(res_command):
    key_plant = res_command
    if check_plant(key_plant):
        plant_dict[key_plant][1] = []  # !!!?


def final_result():
    print("Plants for the exhibition:")
    for key in plant_dict.keys():
        current_rarity = plant_dict[key][0]
        rating = plant_dict[key][1]
        if rating:
            average = sum(plant_dict[key][1]) / len(plant_dict[key][1])
        else:
            average = 0
        print(f"- {key}; Rarity: {current_rarity}; Rating: {average:.2f}")


n = int(input())
plant_dict = {}
for _ in range(n):
    current_plant = input().split('<->')
    plant, rarity = current_plant[0], int(current_plant[1])
    plant_dict[plant] = [rarity, []]

command = input()
while command != 'Exhibition':
    command = command.split(': ')
    if command[0] == 'Rate':
        rate_command(command[1])
    elif command[0] == 'Update':
        update_command(command[1])
    elif command[0] == 'Reset':
        reset_command(command[1])
    command = input()
final_result()
