initial_string = input()

command = input()
while command != 'Easter':
    current_command = command.split()
    if current_command[0] == 'Replace':
        # Here we split the input and get the needed data.
        current_char, new_char = current_command[1], current_command[2]
        initial_string = initial_string.replace(current_char, new_char)
        print(initial_string)
    if current_command[0] == 'Remove':
        # Here we get the substring data.
        substring = current_command[1]
        if substring in initial_string:
            initial_string = initial_string.replace(substring, '')
        print(initial_string)
    if current_command[0] == 'Includes':
        # Here we get the string which the initial string should contain.
        string = current_command[1]
        if string in initial_string:
            print('True')
        else:
            print('False')
    if current_command[0] == 'Change':
        # Here we get the case command.
        case_command = current_command[1]
        if case_command == 'Lower':
            initial_string = initial_string.lower()
        elif case_command == 'Upper':
            initial_string = initial_string.upper()
        print(initial_string)
    if current_command[0] == 'Reverse':
        # Here we get the start and end index
        start_index, end_index = int(current_command[1]), int(current_command[2]) + 1
        if start_index in range(-50, 50) and end_index in range(-50, 50):
            if start_index in range(0, len(initial_string)) and end_index in range(0, len(initial_string)):
                current_piece_of_the_initial_str = initial_string[start_index:end_index]
                new_string = current_piece_of_the_initial_str[::-1]
                print(new_string)

    command = input()
