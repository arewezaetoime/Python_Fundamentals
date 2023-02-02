number_lines = int(input())
capacity = 255
liters_in_the_tank = 0

for command in range(number_lines):
    liters_of_water = int(input())
    if liters_of_water > capacity:
        print('Insufficient capacity!')
        continue
    capacity -= liters_of_water
    liters_in_the_tank += liters_of_water
print(liters_in_the_tank)