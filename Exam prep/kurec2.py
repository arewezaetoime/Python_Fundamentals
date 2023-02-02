vehicles_to_be_tax = input().split('>>')
vehicles_split = ' '.join(vehicles_to_be_tax)
total_tax_collected = 0

for car in vehicles_to_be_tax:
    family_tax = 50
    heavy_duty_tax = 80
    sports_tax = 100
    car_lst = car.split()
    tax_to_pay = 0
    if car_lst[0] == 'family':
        family_tax -= 5 * int(car_lst[1])
        family_tax += 12 * (int(car_lst[2]) // 3000)
        total_tax_collected += family_tax
        tax_to_pay += family_tax
        print(f"A {car_lst[0]} car will pay {tax_to_pay:.2f} euros in taxes.")
    elif car_lst[0] == 'heavyDuty':
        heavy_duty_tax -= 8 * int(car_lst[1])
        heavy_duty_tax += 14 * (int(car_lst[2]) // 9000)
        total_tax_collected += heavy_duty_tax
        tax_to_pay += heavy_duty_tax
        print(f"A {car_lst[0]} car will pay {tax_to_pay:.2f} euros in taxes.")
    elif car_lst[0] == 'sports':
        sports_tax -= 9 * int(car_lst[1])
        sports_tax += 18 * (int(car_lst[2]) // 2000)
        total_tax_collected += sports_tax
        tax_to_pay += sports_tax
        print(f"A {car_lst[0]} car will pay {tax_to_pay:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")



