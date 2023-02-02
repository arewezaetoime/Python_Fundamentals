def multiply(num1, num2):
    return int(num1 * num2)


def divide(num1, num2):
    return int(num1 / num2)


def add(num1, num2):
    return int(num1 + num2)


def subtract(num1, num2):
    return int(num1 - num2)


type_of_operation = input()
number1 = int(input())
number2 = int(input())

if type_of_operation == 'multiply':
    print(multiply(number1, number2))
elif type_of_operation == 'divide':
    print(divide(number1, number2))
elif type_of_operation == 'add':
    print(add(number1, number2))
elif type_of_operation == 'subtract':
    print(subtract(number1, number2))
