people_waiting = int(input())
lift_state = input().split()
lift_int = [int(lift) for lift in lift_state]
starting_index = 0

for person in range(1, people_waiting + 1):
    if lift_int[starting_index] == 4:
        starting_index += 1
    if all(lift_int) == 4 or starting_index >= len(lift_int):
        result = [str(i) for i in lift_int]
        print(f"There isn't enough space! {people_waiting} people in a queue!\n{' '.join(result)}")
        break
    if lift_int[starting_index] <= len(lift_int):
        lift_int[starting_index] += 1
        people_waiting -= 1
result = [str(i) for i in lift_int]
if any(lift_int) < 4:
    print(f"The lift has empty spots!\n{' '.join(result)}")