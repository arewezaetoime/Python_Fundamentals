import re
n = int(input())
pattern = r'^([A-Z][a-z]{2,} [A-Z][a-z]{2,})[#]+(([A-Z][a-z]+[&]?){,3})[\d]{2}(\w+ ([JSC]{3}|[Ltd.]{4}))$'

for _ in range(n):
    current_employee = input()
    result = re.match(pattern, current_employee)
    if result:
        name = result.group(1)
        job_group = result.group(2)
        company = result.group(4)
        # type_company = result.group(5)
        if '&' in result.group(2):
            job_group = result.group(2).replace('&', ' ')
        print(f"{name} is {job_group} at {company}")