text_input = input().split(' ')
concat_text = ''.join(text_input)
our_dict = {}
for char in concat_text:
    if char not in our_dict.keys():
        our_dict[char] = 0
    our_dict[char] += 1

for key, value in our_dict.items():
    print(f"{key} -> {value}")
