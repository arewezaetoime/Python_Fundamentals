encrypted_message = input()

command = input()
while command != 'Decode':
    current_command = command.split('|')
    if current_command[0] == 'Move':
        n_letter = int(current_command[1])
        left_part = encrypted_message[:n_letter]
        right_part = encrypted_message[n_letter:]
        encrypted_message = right_part + left_part
    elif current_command[0] == 'Insert':
        index, value = int(current_command[1]), current_command[2]
        left_side = encrypted_message[:index]
        right_side = encrypted_message[index:]
        encrypted_message = left_side + value + right_side
    elif current_command[0] == 'ChangeAll':
        substring, replacement = current_command[1], current_command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f'The decrypted message is: {encrypted_message}')
