numbers_input = input().split(' ')
numbers_lst_int = list(int(num) for num in numbers_input)
print(f"The minimum number is {min(numbers_lst_int)}")
print(f"The maximum number is {max(numbers_lst_int)}")
print(f"The sum number is: {sum(numbers_lst_int)}")