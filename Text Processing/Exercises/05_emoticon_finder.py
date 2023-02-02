input_string = input()

for index in range(0, len(input_string) - 1):
    if input_string[index] == ':' and index != len(input_string) - 1:
        print(f"{input_string[index]}{input_string[index + 1]}")
