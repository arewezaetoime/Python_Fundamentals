product = input()
quantity = int(input())


def total(param1, param2):
    if param1 == 'coffee':
        price = 1.50
        return param2 * price
    elif param1 == 'water':
        price = 1.00
        return param2 * price
    elif param1 == 'coke':
        price = 1.40
        return param2 * price
    elif param1 == 'snacks':
        price = 2.00
        return param2 * price


print(f"{total(product, quantity):.2f}")
