def palindrome_checker(some_num):
    if some_num == some_num[::-1]:
        return True
    else:
        return False


numbers_input = input().split(', ')
for num in numbers_input:
    if palindrome_checker(num):
        print('True')
    else:
        print('False')

