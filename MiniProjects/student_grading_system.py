students = {
    'takunda':98,
    'promise':78,
    'delight':89,
    'ashebell':76,
    'vannesa':50,
    'rebecca':30,
    'lovedale':43
}

students_grades = students.copy()

for i in students:
    if students[i] >= 90 and students[i] <= 100:
        students_grades[i] = "A+"
    elif students[i] >= 80 and students[i] < 90:
        students_grades[i] = "A"
    elif students[i] >= 70 and students[i] < 80:
        students_grades[i] = "B+"
    elif students[i] >= 60 and students[i] < 70:
        students_grades[i] = "B"
    elif students[i] >= 50 and students[i] < 60:
        students_grades[i] = "C"
    elif students[i] >= 40 and students[i] < 50:
        students_grades[i] = "D"
    else:
        students_grades[i] = "F"

print(students_grades)
