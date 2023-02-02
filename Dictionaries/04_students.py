students = {}

input_student = input().split(':')

while len(input_student) > 1:
    course = input_student[2]
    name_id = f"{input_student[0]} - {input_student[1]}"
    if course not in students.keys():
        students[course] = []
    students[course].append(name_id)
    input_student = input().split(':')

searched_course = input_student[0].replace('_', ' ')
for student in students[searched_course]:
    print(student)
