elements = input().split(' ')
dictionary = {}

for word in elements:
    lower_word = word.lower()
    if lower_word not in dictionary:
        dictionary[lower_word] = 0
    dictionary[lower_word] += 1

for key in dictionary.keys():
    if dictionary[key] % 2 == 1:
        print(key, end=' ')
