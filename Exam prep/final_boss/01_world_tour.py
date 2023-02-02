starting_string = input()

command = input()
while command != 'Travel':
    current_command = command.split(':')
    if current_command[0] == 'Add Stop':
        current_command, index, string = current_command[0], int(current_command[1]), current_command[2]
        if index < len(starting_string):
            starting_string = starting_string[:index] + string + starting_string[index:]
        print(starting_string)
    elif current_command[0] == 'Remove Stop':
        current_command, start_index, end_index = current_command[0], int(current_command[1]), \
                                                  int(current_command[2]) + 1
        if start_index < len(starting_string) and end_index <= len(starting_string):
            left_side, right_side = starting_string[:start_index], starting_string[end_index:]
            starting_string = left_side + right_side
        print(starting_string)
    elif current_command[0] == 'Switch':
        if current_command[1] in starting_string:
            current_command, old_string, new_string = current_command[0], current_command[1], current_command[2]
            starting_string = starting_string.replace(old_string, new_string)
        print(starting_string)

    command = input()
print(f"Ready for world tour! Planned stops: {starting_string}")