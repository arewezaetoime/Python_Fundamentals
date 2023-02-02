def even(some_numbers):
    return [str(digit) for digit in some_numbers if digit % 2 == 0]


def odd(some_numbers):
    return [str(digit) for digit in some_numbers if digit % 2 == 1]


def positive(some_numbers):
    return [str(digit) for digit in some_numbers if digit >= 0]


def negative(some_numbers):
    return [str(digit) for digit in some_numbers if digit < 0]


numbers = [int(number) for number in input().split(', ')]
print(f"Positive: {', '.join(positive(numbers))}")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")
