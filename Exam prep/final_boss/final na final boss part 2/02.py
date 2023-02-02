import re
n = int(input())
pattern = r'^(.+)>([0-9]+)\|([a-z]+)\|([A-Z]+)\|([^<]+)<\1$'

for _ in range(n):
    current_pass = input()
    match = re.search(pattern, current_pass)
    if match:
        number = match.group(2)
        let_low = match.group(3)
        let_up = match.group(4)
        symbols = match.group(5)
        decrypted = number + let_low + let_up + symbols
        print(f'Password: {decrypted}')
    else:
        print('Try another password!')