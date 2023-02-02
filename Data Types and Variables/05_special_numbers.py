n = int(input())

for num in range(1, n + 1):
    current_sum = 0
    digits = num
    while digits > 0:
        current_sum += digits % 10
        digits = int(digits / 10)
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')