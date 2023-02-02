# Here we receive keys
current_keys = input().split()
lines_to_decrypt = []
decrypted_lines = []
# Here we receive lines of string to decrypt
current_line = input()
while current_line != 'find':
    lines_to_decrypt.append(current_line)

    current_line = input()
# Here we start looping through lines of string and decrypt what we can.
for string in lines_to_decrypt:
    decrypted_line = ''
    key_index_counter = 0
    for letter in string:
        # Here we decrypt letter by letter using the respective key for every letter in row, and when the keys hit
        # their max we revert the sequence back again from the initial start
        decrypted_letter = ord(letter) - int(current_keys[key_index_counter])
        decrypted_line += chr(decrypted_letter)
        key_index_counter += 1
        if key_index_counter == len(current_keys):
            key_index_counter = 0
    decrypted_lines.append(decrypted_line)
# Here we start to extract the needed data from every decrypted string. One by one.
for final_line in decrypted_lines:
    start_index_metal = final_line.index('&')
    start_index_coordinates = final_line.index('<')
    type_previous_metal = ''
    coordinates = ''
    # Here we start looping through decrypted line of string to collect the type of metal letters.
    for letter_type in range(start_index_metal + 1, len(final_line) - 1):
        if final_line[letter_type] == '&':
            break
        else:
            type_previous_metal += final_line[letter_type]
    # Here we start looping through the decrypted line of string to collect the coordinate letters.
    for letter_coordinates in range(start_index_coordinates + 1, len(final_line) - 1):
        if final_line[letter_coordinates] == '>':
            break
        else:
            coordinates += final_line[letter_coordinates]
    # Here we print the result if there's any.
    if type_previous_metal and coordinates:
        print(f"Found {type_previous_metal} at {coordinates}")