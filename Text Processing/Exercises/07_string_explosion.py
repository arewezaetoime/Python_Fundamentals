starting_string = input()
new_string = ''
strength = 0
for index in range(len(starting_string)):
    if strength > 0 and starting_string[index] != '>':
        strength -= 1
    elif starting_string[index] == '>':
        new_string += starting_string[index]
        strength += int(starting_string[index + 1])
    else:
        new_string += starting_string[index]

print(new_string)