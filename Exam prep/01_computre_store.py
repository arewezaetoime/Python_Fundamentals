special = 'special'
regular = 'regular'

current_sum = 0
# regular_tax = current_sum * 0.2
# total_sum = current_sum + regular_tax
while True:
    regular_tax = current_sum * 0.2
    total_sum = current_sum + regular_tax
    command = input()
    if command == special:
        if total_sum == 0:
            print('Invalid order!')
            break
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {current_sum:.2f}$\n\
        Taxes: {regular_tax:.2f}$\n-----------\nTotal price: {total_sum - (total_sum * 0.1):.2f}$")
        break
    elif command == regular:
        if current_sum == 0:
            print('Invalid order!')
            break
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {current_sum:.2f}$\n\
                Taxes: {regular_tax:.2f}$\n-----------\nTotal price: {total_sum:.2f}$")
        break

    command = float(command)
    if command < 0:
        print('Invalid price!')
    else:
        current_sum += command
