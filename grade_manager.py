student_name = input("Enter student name: ")

grades = []

for i in range(3):
    grade = float(input(f"Enter grade {i + 1}: "))
    grades.append(grade)

average = sum(grades) / len(grades)

print("\nStudent:", student_name)
print("Grades:", grades)
print("Average grade:", average)
