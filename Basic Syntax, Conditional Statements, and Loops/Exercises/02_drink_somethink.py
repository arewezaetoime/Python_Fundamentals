persons_age = int(input())
drink = ''
if persons_age <= 14:
    drink = 'toddy'
elif persons_age <= 18:
    drink = 'coke'
elif persons_age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'
print(f'drink {drink}')
