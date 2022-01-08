import random

names = ["Karan", "Kaushik", "Priyanka", "Karmarkar", "Dilip", "Khushi", "Bharati"]

students_scores = {student:random.randint(50,100) for student in names}

print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 75}

print(passed_students)