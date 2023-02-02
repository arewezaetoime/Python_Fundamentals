n = int(input())
numbers = []
filtered = []

COMMAND_EVEN = 'even'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'
COMMAND_ODD = 'odd'

for num in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

for number in numbers:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_POSITIVE and number >= 0) or
        (command == COMMAND_NEGATIVE and number < 0)
    )
    if filtered_passes:
        filtered.append(number)

print(filtered)