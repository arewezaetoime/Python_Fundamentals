import re
sentence = input()
magic_word = input()
pattern = fr'(?i)\b{magic_word}\b'
result = re.findall(pattern, sentence)
print(len(result))
