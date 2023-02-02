starting_metres = 5364
everest = 8848
days_counter = 1
command = input()
metres_for_the_day = int(input())
while True:
    if command != 'END':
        if days_counter == 5 or starting_metres >= everest:
            break
        if command == 'Yes':
            days_counter += 1
            starting_metres += metres_for_the_day
        elif command == 'No':
            starting_metres += metres_for_the_day
        command = input()
        metres_for_the_day = int(input())
    else:
        break


if starting_metres >= everest:
    print(f"Goal reached for {days_counter} days!")
else:
    print('Failed!')
    print(f'{starting_metres}')