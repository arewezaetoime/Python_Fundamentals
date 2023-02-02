def smallest_num_checker(first, second, third):
    return min(first, second, third)


first_number, second_number, third_number = int(input()), int(input()), int(input())
print(smallest_num_checker(first_number, second_number, third_number))