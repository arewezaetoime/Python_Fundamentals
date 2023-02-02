initial_values = input().split()
integer_array = [int(integer) for integer in initial_values]

while True:
    command = input().split()
    if command[0] == "end":
        break

    if 'swap' in command:
        swap1 = int(command[1])
        swap2 = int(command[2])
        integer_array[swap1], integer_array[swap2] = integer_array[swap2], integer_array[swap1]

    if 'multiply' in command:
        multiply1 = int(command[1])
        multiply2 = int(command[2])
        integer_array[multiply1] = integer_array[multiply1] * integer_array[multiply2]

    if 'decrease' in command:
        for element in range(len(integer_array)):
            poped = integer_array.pop(element)
            poped -= 1
            integer_array.insert(element, poped)

print(*integer_array, sep=', ')