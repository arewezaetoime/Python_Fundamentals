def greater_than_average(numbers):
    average_number = sum(numbers) / len(numbers)
    greater_numbers = []

    for integer in numbers:
        if integer > average_number:
            greater_numbers.append(integer)
    if len(greater_numbers) == 0:
        return 'No'
    elif len(greater_numbers) > 5:
        top_five = []
        for top in sorted(greater_numbers, reverse=True):
            top_five.append(top)
            if len(top_five) == 5:
                break
        return top_five
    else:
        return greater_numbers


numbers_lst = input().split()
integers_lst = [int(number) for number in numbers_lst]
result = greater_than_average(integers_lst)
result = sorted(result, reverse=True)
if greater_than_average(integers_lst) == 'No':
    print('No')
else:
    print(*result)