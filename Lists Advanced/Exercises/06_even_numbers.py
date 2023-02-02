number = list(map(int, input().split(', ')))
found_indices = map(lambda x: x if number[x] % 2 == 0 else 'no', range(len(number)))
even_numbers = list(filter(lambda x: x != 'no', found_indices))
print(even_numbers)
