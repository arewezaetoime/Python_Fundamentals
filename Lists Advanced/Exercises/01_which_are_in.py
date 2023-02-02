first_sequence = input().split(', ')
second_sequence = input().split(', ')
new_sequence = []
for first in first_sequence:
    for second in second_sequence:
        if first in second:
            new_sequence.append(first)
            break
print(new_sequence)