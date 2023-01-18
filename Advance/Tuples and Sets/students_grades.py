n = int(input())
student_data = {}
for number in range(1, n+1):
    student, grade = input().split(" ")
    if student not in student_data:
        student_data[student] = []

    student_data[student].append(float(grade))

for students, grades in student_data.items():
    convert_grades = ' '.join(map(lambda grade: f"{grade:.2f}", grades))
    average_grade = sum(grades)/len(grades)
    print(f"{students} -> {convert_grades} (avg: {average_grade:.2f})")

