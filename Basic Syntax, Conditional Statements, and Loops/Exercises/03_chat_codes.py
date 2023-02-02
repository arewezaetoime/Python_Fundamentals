number_messages = int(input())
for message in range(number_messages):
    temp = ''
    command = int(input())
    if command == 88:
        temp = 'Hello'
    elif command == 86:
        temp = 'How are you?'
    elif command < 88:
        temp = 'GREAT!'
    elif command > 88:
        temp = 'Bye.'
    print(temp)


