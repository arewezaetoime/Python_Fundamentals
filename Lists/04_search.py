number_lines = int(input())
magic_word = input()
words_lst = []
magic_lst = []
for _ in range(number_lines):
    words = input()
    words_lst.append(words)
for i in words_lst:
    if magic_word in i:
        magic_lst.append(i)
print(words_lst)
print(magic_lst)
