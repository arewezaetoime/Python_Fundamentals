# Taking inputs
starting_char = input()
ending_char = input()
line_of_text = input()
# Here we find the indexes/boundaries of what we want to extract of the text.
start_index = ord(starting_char)
end_index = ord(ending_char)
total_sum = 0
found_chars = []
if start_index in range(0, 127) and end_index in range(1, 127):
    for char in line_of_text:
        if ord(char) in range(start_index, end_index):
            found_chars.append(char)
            total_sum += ord(char)
print(total_sum)
# print(' '.join(found_chars))