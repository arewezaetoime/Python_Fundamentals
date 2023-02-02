list_of_characters = input().split(', ')
dictionary = {key: ord(key) for key in list_of_characters}
print(dictionary)