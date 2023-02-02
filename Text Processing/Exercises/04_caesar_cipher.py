starting_input = input()
encrypted_text = ''
for char in starting_input:
    new_char = ord(char) + 3
    encrypted_text += chr(new_char)

print(encrypted_text)