concealed_message = input()

command = input()
while command != 'Reveal':
    command = command.split(':|:')
    if command[0] == 'InsertSpace':
        index = int(command[1])
        left_side, right_side = concealed_message[:index], concealed_message[index:]
        concealed_message = left_side + ' ' + right_side
        print(concealed_message)
    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")
