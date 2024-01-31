students = {}
n = int(input("Enter the no.of students :"))

for i in range(n):
    name = input("Enter the name :")
    age = int(input("Enter the age :"))
    grade = input("Enter the grade :")
    students[name] = age,grade

print(students)