number_words = int(input())
my_dictionary = {}
for i in range(1, number_words + 1):
    word = input()
    synonym = input()
    if word not in my_dictionary.keys():
        my_dictionary[word] = []
    my_dictionary[word].append(synonym)

for pr in my_dictionary.keys():
    print(f"{pr} - {', '.join(my_dictionary[pr])}")
