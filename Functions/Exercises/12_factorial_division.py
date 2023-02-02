def first_factorial(first):
    factorial = 1
    for mult in range(first - 1, 0, -1):
        factorial = factorial * mult
    return factorial * first


def second_factorial(second):
    factorial = 1
    for mult in range(second - 1, 0, -1):
        factorial = factorial * mult
    return factorial * second


first_number = int(input())
second_number = int(input())
result = first_factorial(first_number) / second_factorial(second_number)
print(f'{result:.2f}')