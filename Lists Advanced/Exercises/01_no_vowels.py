text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I', 'A']
new_text = ''.join([x for x in text if x not in vowels])
print(new_text)
