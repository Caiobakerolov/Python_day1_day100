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
for student in student_scores:

    score = student_scores[student]

    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Imprime o dicionário de grades no final
print(student_grades)
