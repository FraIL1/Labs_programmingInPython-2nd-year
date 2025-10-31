student = {
    "name": "Артем",
    "age": 19,
    "course": "Программирование на Python",
    "grades": [4, 5, 3, 5, 4]
}

print(student['name'], student['course'], sep=', ')

average_grade = sum(student['grades']) / len(student['grades'])
print(f"Средний балл: {average_grade}")

student['grades'].append(5)

print(student)
