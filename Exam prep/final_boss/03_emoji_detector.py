import re
our_input = input()
pattern = r':{2}[A-Z][a-z]{2,}:{2}|\*{2}[A-Z][a-z]{2,}\*{2}'
threshold = 1
coolness_digits = re.findall(r'\d', our_input)
cool_emojis = re.findall(pattern, our_input)
for digit in coolness_digits:
    threshold *= int(digit)
print(f'Cool threshold: {threshold}')
print(f'{len(cool_emojis)} emojis found in the text. The cool ones are:')
for current_emoji in cool_emojis:
    cool_point = 0
    for letter in current_emoji:
        if letter == ':' or letter == '*':
            continue
        else:
            cool_point += ord(letter)
    if cool_point > threshold:
        print(current_emoji)