from collections import namedtuple

number_student = int(input())
Student = namedtuple("Student", input().split())
student_list = [Student(*input().split()) for _ in range(number_student)]
average_mark = sum([int(student.MARKS) for student in student_list]) / number_student
print(f"{average_mark:.2f}")
