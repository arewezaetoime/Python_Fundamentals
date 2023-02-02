numbers_as_string = input().split(' ')
numbers_as_integers = list(int(num) for num in numbers_as_string)
result = sorted(numbers_as_integers)
print(result)