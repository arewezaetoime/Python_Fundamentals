numbers_input = input().split()
numbers_to_remove = int(input())
integer_list = []
for number in numbers_input:
    integer_list.append(int(number))
for remove in range(numbers_to_remove):
    integer_list.remove(min(integer_list))
print(*integer_list, sep=', ')
