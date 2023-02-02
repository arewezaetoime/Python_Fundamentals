def characters_between(first, second):
    characters = []
    for character in range(ord(first) + 1, ord(second)):
        characters.append(chr(character))
    return ' '.join(characters)


first_character = input()
second_character = input()
print(characters_between(first_character, second_character))