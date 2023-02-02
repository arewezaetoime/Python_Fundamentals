def absolute_values(num):
    absolute_list = []
    for number in numbers:
        number = abs(float(number))
        absolute_list.append(number)
    return absolute_list


numbers = input().split(' ')
print(absolute_values(numbers))