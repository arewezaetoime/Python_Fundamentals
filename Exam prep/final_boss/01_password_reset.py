initial_string = input()
command = input()

while command != 'Done':
    current_command = command.split()
    if current_command[0] == 'TakeOdd':
        initial_string = ''.join(initial_string[x] for x in range(len(initial_string)) if x % 2 != 0)
        print(initial_string)
    elif current_command[0] == 'Cut':
        index, length = int(current_command[1]), int(current_command[2])
        sub = index + length
        # cutstring = new_password[index:sub]
        initial_string = initial_string[:index] + initial_string[sub:]
        print(initial_string)
    elif current_command[0] == 'Substitute':
        substring, substitute = current_command[1], current_command[2]
        if substring in initial_string:
            initial_string = initial_string.replace(substring, substitute)
            print(initial_string)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {initial_string}")