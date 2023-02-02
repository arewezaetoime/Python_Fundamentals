import re
destinations_input = input()
pattern = r'([=|\/])([A-Z][A-Za-z]{2,})\1'
results = re.findall(pattern, destinations_input)

destinations = []
travel_point = 0
if results:
    for destination in results:
        destinations.append(destination[1])
        travel_point += len(destination[1])

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {travel_point}')



