parking = {}

number_cars = int(input())

for car in range(number_cars):
    current_car = input().split()
    command = current_car[0]
    username = current_car[1]
    if command == 'register':
        license_plate = current_car[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif command == 'unregister':
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for user, plate in parking.items():
    print(f"{user} => {plate}")