def drive(current_car, current_distance, current_fuel):
    if car_collection[current_car][1] < current_fuel:
        print("Not enough fuel to make that ride")
    else:
        car_collection[current_car][0] += current_distance
        car_collection[current_car][1] -= current_fuel
        print(f"{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.")
    if car_collection[current_car][0] >= 100_000:
        del car_collection[current_car]
        print(f"Time to sell the {current_car}!")


def refuel(car, fuel):
    litres_used = 0
    for _ in range(fuel):
        if car_collection[car][1] == 75:
            break
        car_collection[car][1] += 1
        litres_used += 1
    print(f"{car} refueled with {litres_used} liters")


def revert(car, kilometres):
    car_collection[car][0] -= kilometres
    print(f"{car} mileage decreased by {kilometres} kilometers")


def final_print(our_collection ):
    for car in car_collection.keys():
        print(f"{car} -> Mileage: {our_collection[car][0]} kms, Fuel in the tank: {our_collection[car][1]} lt.")


n = int(input())
car_collection = {}
for _ in range(n):
    current_input = input().split('|')
    car, mileage, fuel = current_input[0], int(current_input[1]), int(current_input[2])
    car_collection[car] = [mileage, fuel]

command = input()
while command != 'Stop':
    current_command = command.split(' : ')
    if current_command[0] == 'Drive':
        car, distance, fuel = current_command[1], int(current_command[2]), int(current_command[3])
        drive(car, distance, fuel)
    elif current_command[0] == 'Refuel':
        car, fuel = current_command[1], int(current_command[2])
        refuel(car, fuel)
    elif current_command[0] == 'Revert':
        car, kilometres = current_command[1], int(current_command[2])
        if car_collection[car][0] - kilometres >= 10_000:
            revert(car, kilometres)
        else:
            car_collection[car][0] = 10_000
    command = input()

final_print(car_collection)