employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())
total_debit = employee_one + employee_two + employee_three
hours_counter = 0
while students > 0:
    students -= total_debit
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter += 1
        continue
print(f"Time needed: {hours_counter}h.")

