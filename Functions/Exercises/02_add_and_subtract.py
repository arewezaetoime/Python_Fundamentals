def sum_numbers(first, second):
    return first + second


def subtract(first, second):
    return first - second


def add_and_subtract(first, second, third):
    sum_of_two = sum_numbers(first, second)
    sub_by_third = subtract(sum_of_two, third)
    return sub_by_third


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))