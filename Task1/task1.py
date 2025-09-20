class Student:
    def __init__(self, name, group, grades):

        self.name = name
        self.group = group
        self.grades = list(map(int, grades))

    def average_grade(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0

    def is_excellent(self):
        return self.average_grade() >= 4.5

    def __str__(self):
        return f'{self.name} - {self.group}'


def main():
    with open('students.txt', 'r', encoding='utf-8') as f:
        students = []
        for line in f:
            name, group, grades = line.strip().split(';')
            students.append(Student(name, group, grades.split(',')))

    excellent = [s for s in students if s.is_excellent()]

    with open('excellent_students.txt', 'w', encoding='utf-8') as f:
        for s in excellent:
            f.write(f'{s.name} - {s.group}\n')

    groups = {}
    for s in students:
        groups[s.group] = groups.setdefault(s.group, []) + [s.average_grade()]


    print("Средний балл по группам:")
    for group, grades in groups.items():
        print(f'Группа {group}: {sum(grades)/len(grades):.3f}')


if __name__ == "__main__":
    main()