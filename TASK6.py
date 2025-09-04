#Student Gradebook Analyzer
"""
TP:
I will prompt user to enter the number of subjects and fix that for all students.
    The rest is straightforward
"""
grade_book = {}
repeat = True
print("Welcome to Student Gradebook Analyzer\n")
num_sub = int(input("Please enter the number of subjects: "))
num_stu = int(input("Enter number of students: "))

for i in range(num_stu):
    entry  = input("Please input student name followed by grades: \n e.g: \"Ali 87 73 92\"\n Entry: ")
    list_entry= entry.split(" ",1)
    #defining dictionary as asked in question
    grade_book[list_entry[0]] = list_entry[1]

class_avg = 0
for student in grade_book:
    stu_avg = 0
    separate_grades = grade_book[student].split()
    for grade in separate_grades:
        stu_avg = stu_avg + int(grade)
    stu_avg = stu_avg / num_sub
    #modifying dict values to hold student averages instead
    grade_book[student] = stu_avg
    print(f"{student}'s average = {stu_avg}")
    class_avg = class_avg + stu_avg

class_avg = class_avg / num_stu
print(f"\nThe class average = {class_avg}")

#printing those above:
for student in grade_book:
    if grade_book[student] > class_avg:
        print(f"{student} is above class average")
