numbers = input().split(' ')
rounded = []

for number in numbers:
    number = round(float(number))
    rounded.append(number)
print(rounded)
