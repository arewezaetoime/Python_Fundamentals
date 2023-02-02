import random
# toto = [random.randint(1, 49)
#         for luck in range(6)]
numbers = []
while len(numbers) < 6:
    lucky_number = random.randint(1, 49)
    if lucky_number not in numbers:
        numbers.append(lucky_number)
print('----------------')
print('****************')
print(*numbers)
print('****************')
print('----------------')

