start_index = int(input())
final_index = int(input())

for char in range(start_index, final_index + 1):
    print(f'{chr(char)}', end=' ')