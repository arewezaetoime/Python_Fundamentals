number_lines = int(input())
positives = []
negatives = []
for number in range(number_lines):
    current_number = int(input())
    if current_number < 0:
        negatives.append(current_number)
    else:
        positives.append(current_number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
