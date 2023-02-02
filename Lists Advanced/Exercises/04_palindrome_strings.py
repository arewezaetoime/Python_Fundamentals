words = input().split(' ')
palindrome = input()
palindrome_lst = []
for word in words:
    if word == ''.join(reversed(word)):
        palindrome_lst.append(word)
print(palindrome_lst)
print(f"Found palindrome {palindrome_lst.count(palindrome)} times")