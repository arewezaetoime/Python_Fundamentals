number_times = int(input())

for first_char in range(number_times):
    for second_char in range(number_times):
        for third_char in range(number_times):
            print(f'{chr(97 + first_char)}{chr(97 + second_char)}{chr(97 + third_char)}')
