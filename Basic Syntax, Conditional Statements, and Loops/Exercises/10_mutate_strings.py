first_string = input()
second_string = input()

current_string = first_string
current = ''
for character in range(len(first_string)):
    left = second_string[:character + 1]
    right = first_string[character + 1:]
    current = left + right
    if current == current_string:
        continue
    else:
        print(current)
        current_string = current
