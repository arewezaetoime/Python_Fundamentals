import string
strin = input()
while strin != 'stop':
    for i in strin[1::]:
        print(i, end='')
    print()
    strin = input()