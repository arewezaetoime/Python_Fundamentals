import re
dates = input()
regex = r'\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b'
results = re.findall(regex, dates)
for current_date in results:
    print(f'Day: {current_date[0]}, Month: {current_date[2]}, Year: {current_date[3]}')
