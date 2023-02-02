number_of_rooms = int(input())
free_chairs = []
needed_chairs = []
total_people = 0
for room in range(1, number_of_rooms + 1):
    current_room = input().split(' ')
    chairs, people = current_room[0], int(current_room[1])
    total_people += people
    if len(chairs) >= people:
        free_chairs.append(abs(len(chairs) - people))
    elif people > len(chairs):
        print(f"{abs(people - len(chairs))} more chairs needed in room {room}")
        needed_chairs.append(abs(people - len(chairs)))
if sum(needed_chairs) == 0:
    print(f"Game On, {sum(free_chairs)} free chairs left")
