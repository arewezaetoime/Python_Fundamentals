def abjuration_func(spell):
    spell = spell.upper()
    print(spell)
    return spell


def necromancy_func(spell):
    spell = spell.lower()
    print(spell)
    return spell


def illusion_func(spell, index, letter):
    if index in range(0, len(spell)):
        old_letter = spell[index]
        spell = spell.replace(old_letter, letter)
        print('Done!')
        return spell
    else:
        print('The spell was too weak.')


def divination_func(spell, first_sub, second_sub):
    spell = spell.replace(first_sub, second_sub)
    print(spell)
    return spell


def alteration_func(spell, substring):
    spell = spell.replace(substring, '')
    print(spell)
    return spell


list_of_commands = ["Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]
spell = input()

command = input()
while command != 'Abracadabra':
    current_command = command.split()
    if current_command[0] in list_of_commands:
        if current_command[0] == list_of_commands[0]:
            abjuration_func(spell)

        elif current_command[0] == list_of_commands[1]:
            necromancy_func(spell)

        elif current_command[0] == list_of_commands[2]:
            index, letter = int(current_command[1]), current_command[2]
            illusion_func(spell, index, letter)

        elif current_command[0] == list_of_commands[3]:
            first_sub, second_sub = current_command[1], current_command[2]
            if first_sub in spell:
                divination_func(spell, first_sub, second_sub)

        elif current_command[0] == list_of_commands[4]:
            substring = current_command[1]
            if substring in spell:
                alteration_func(spell, substring)

    else:
        print('The spell did not work!')

    command = input()
