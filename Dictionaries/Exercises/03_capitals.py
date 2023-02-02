countries = input().split(', ')
capitals = input().split(', ')
final_dict = dict(zip(countries, capitals))
for county, city in final_dict:
    print(f"{county} -> {city}")

