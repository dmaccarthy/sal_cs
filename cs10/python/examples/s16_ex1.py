"""
CSE 1120: Structured Programming
Accumulation
Example 1

"""

from sal_sp2 import marks_list

# Initialize accumulators
student = 0
grade_A = 0
total_marks = 0

# Iterate
template = "Student {} earned a mark of {}."
for mark in marks_list:
    student += 1         # Count students
    if mark >= 80:       # Count students with an 'A'
        grade_A += 1
    total_marks += mark  # Total marks
    print(template.format(student, mark))

# Output totals
print("\nStudents =", student)
print("Total =", total_marks)
print("Average =", total_marks / student)
print("Students with an A =", grade_A)
