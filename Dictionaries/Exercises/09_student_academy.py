score_book = {}
number_students = int(input())

for _ in range(number_students):
    current_student = input()
    current_grade = float(input())
    if current_student not in score_book.keys():
        score_book[current_student] = []
    score_book[current_student].append(current_grade)

    # average_score = sum(score_book[current_student]) / len(score_book[current_student])
    # if average_score < 4.50:
    #     del score_book[current_student]


for student, grade in score_book.items():
    average_grade = sum(score_book[student]) / len(score_book[student])
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")

# filtered_dict = {person: grade for (person,grade) in score_book.items() if sum(score_book[person]) / len(score_book[person]) >= 4.50}
# print(filtered_dict)
# print(score_book)


