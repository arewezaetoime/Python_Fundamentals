from forex_python.converter import CurrencyRates
amount = int(input('Amount in GBP: '))
c = CurrencyRates()
current_rate = c.get_rates('GBP', 'USD')
result = amount * current_rate
print(f'{amount} GBP equals to {result:.3f} USD')