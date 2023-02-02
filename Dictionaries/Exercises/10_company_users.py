companies_dict = {}

current_command = input().split(' -> ')
while len(current_command) > 1:
    company = current_command[0]
    employee = current_command[1]
    if company not in companies_dict.keys():
        companies_dict[company] = []
    if employee in companies_dict[company]:
        current_command = input().split(' -> ')
        continue

    companies_dict[company].append(employee)
    current_command = input().split(' -> ')

for current_company in companies_dict.keys():
    print(f"{current_company}")
    for current_employee in companies_dict[current_company]:
        print(f"-- {''.join(current_employee)}")
