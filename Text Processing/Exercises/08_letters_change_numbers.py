numbers_input = [number.strip() for number in input().split()]
alphabet = {}
char = 97
for alpha in range(1, 26 + 1):
    alphabet[chr(char)] = alpha
    char += 1
total_sum = 0
for current_number in numbers_input:
    number_to_use = int(current_number[1:-1])
    current_sum = 0
    if current_number[:1].isupper():
        current_sum = number_to_use / alphabet[current_number[0].lower()]
    elif current_number[:1].islower():
        current_sum = number_to_use * alphabet[current_number[0].lower()]
    if current_number[-1:].isupper():
        current_sum -= alphabet[current_number[-1:].lower()]
    elif current_number[-1:].islower():
        current_sum += alphabet[current_number[-1:].lower()]
    total_sum += current_sum
print(f'{total_sum: .2f}')
