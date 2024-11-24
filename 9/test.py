# Dicionário inicial fornecido
student_scores = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 99,
    "Diana": 65,
}

# Novo dicionário para guardar as notas convertidas
student_grades = {}

# Percorrer o dicionário de notas
for student, score in student_scores.items():
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Imprime o dicionário de grades no final
print(student_grades)
