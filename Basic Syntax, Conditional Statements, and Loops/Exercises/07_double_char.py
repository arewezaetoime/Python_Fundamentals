command = input()

while command != 'End':
    if command != 'SoftUni':
        for i in command[::1]:
            i = i * 2
            print(i, end='')
        print()
    command = input()
