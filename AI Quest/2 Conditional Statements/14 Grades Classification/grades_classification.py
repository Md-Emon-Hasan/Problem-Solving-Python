# 14. Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

# Take student percentage as input
percentage = float(input("Enter student's percentage: "))

# Determine grade
if percentage >= 90:
    grade = "A+"
elif 80 <= percentage < 90:
    grade = "A"
elif 70 <= percentage < 80:
    grade = "B"
elif 60 <= percentage < 70:
    grade = "C"
else:
    grade = "Fail"

print(f"Student's grade is: {grade}")