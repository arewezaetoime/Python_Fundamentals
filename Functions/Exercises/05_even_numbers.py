def even_number_sorter(numbers):
    return numbers % 2 == 0


numbers_lst = input().split()
numbers_integers = list(int(num) for num in numbers_lst)
even_numbers_lst = filter(even_number_sorter, numbers_integers)
print(list(even_numbers_lst))