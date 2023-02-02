activation_key = input()

command = input()
while command != 'Generate':
    command = command.split('>>>')
    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print("Substring not found!")
    elif command[0] == 'Flip':
        current_case, start_index, end_index = command[1], int(command[2]), int(command[3])
        if current_case == 'Upper':
            current_cut = activation_key[start_index:end_index].upper()
            activation_key = activation_key.replace(activation_key[start_index:end_index], current_cut)
            print(activation_key)

        elif current_case == 'Lower':
            current_cut = activation_key[start_index:end_index].lower()
            activation_key = activation_key.replace(activation_key[start_index:end_index], current_cut)
            print(activation_key)
    elif command[0] == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        string_to_slice = activation_key[start_index:end_index]
        activation_key = activation_key.replace(string_to_slice, '')
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")

