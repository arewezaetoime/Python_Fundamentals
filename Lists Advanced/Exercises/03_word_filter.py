words = input().split(' ')
filtered = [word for word in words if len(word) % 2 == 0]
print('\n'.join(filtered))
