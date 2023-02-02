single_input = input()

last_letter = ''
final_text = ''

for char in single_input:
    if char != last_letter:
        final_text += char
        last_letter = char
print(final_text)