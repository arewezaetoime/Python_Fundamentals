def add_func(person, hp, mana):
    if person not in our_dict.keys():
        our_dict[person] = []
        our_dict[person].append(hp)
        our_dict[person].append(mana)
    elif person in our_dict.keys():
        our_dict[person][0] += hp


def attack_func(attacker, defender, dmg):
    if attacker in our_dict.keys() and defender in our_dict.keys():
        our_dict[defender][0] -= dmg
        our_dict[attacker][1] -= 1
        if our_dict[defender][0] <= 0:
            del our_dict[defender]
            print(f"{defender} was disqualified!")
        if our_dict[attacker][1] <= 0:
            del our_dict[attacker]
            print(f"{attacker} was disqualified!")


def delete_func(user):
    if user in our_dict.keys():
        del our_dict[user]
    if user == 'All':
        our_dict.clear()


def print_func():
    print(f"People count: {len(our_dict.keys())}")
    for current_user, values in our_dict.items():
        hp = values[0]
        mana = values[1]
        print(f'{current_user} - {hp} - {mana}')


our_dict = {}

command = input()
while command != 'Results':
    command = command.split(':')
    if command[0] == 'Add':
        person_name, health, energy = command[1], int(command[2]), int(command[3])
        add_func(person_name, health, energy)
    elif command[0] == 'Attack':
        attacker_name, defender_name, damage = command[1], command[2], int(command[3])
        attack_func(attacker_name, defender_name, damage)
    elif command[0] == 'Delete':
        username = command[1]
        delete_func(username)
    command = input()

print_func()
