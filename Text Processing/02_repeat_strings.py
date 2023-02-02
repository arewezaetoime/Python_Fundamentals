text_sequence = input().split()

for text in text_sequence:
    print(text * len(text), end='')