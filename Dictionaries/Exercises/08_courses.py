courses = {}

current_student = input().split(' : ')
while len(current_student) > 1:
    course = current_student[0]
    student = current_student[1]
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)

    current_student = input().split(' : ')

for current_course in courses.keys():
    print(f"{current_course}: {len(courses[current_course])}")
    for stud in courses[current_course]:
        print(f"-- {''.join(stud)}")
