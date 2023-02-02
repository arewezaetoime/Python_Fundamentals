spell = input()
list_of_commands = ["Abracadabra", "Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]
command = input()
while command != 'Abracadabra':
    command = command.split()
    if command[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)
    if command[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)
    if command[0] == 'Illusion':
        index, letter = int(command[1]), command[2]
        if index in range(0, len(spell)):
            current_letter = spell[index]
            spell = spell.replace(current_letter, letter)
            print('Done!')
        else:
            print('The spell was too weak.')
    if command[0] == 'Divination':
        first_string, second_string = command[1], command[2]
        if first_string in spell:
            spell = spell.replace(first_string, second_string)
            print(spell)
    if command[0] == 'Alteration':
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, "", 1)
            print(spell.strip())
    if command[0] not in list_of_commands:
        print('The spell did not work!')
    command = input()