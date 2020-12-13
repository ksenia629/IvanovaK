def print_students(students):
    print(u"Имя".ljust(10), u"Фамилия".ljust(10),
          u"Экзамены".ljust(50), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(10),
              student["surname"].ljust(10), str(student["exams"]).ljust(50),
              str(student["marks"]).ljust(20))


def filter(groupmates, sb):
    id = 0
    idd = []
    for groupmate in groupmates:
        id =int( id + 1)
        ss = 0

        for mark in groupmate["marks"]:
            ss = ss + mark
        ss = ss / 3

        if ss >= sb:
            idd.append(id)
    return idd


groupmates = [
     {
     "name": "Александр",
     "surname": "Иванов",
     "exams": ["Информатика", "ЭЭиС", "Web"],
     "marks": [4, 3, 5]
     },
     {
     "name": "Иван",
     "surname": "Петров",
     "exams": ["История", "АиГ", "КТП"],
     "marks": [4, 4, 4]
     },
     {
     "name": "Кирилл",
     "surname": "Смирнов",
     "exams": ["Философия", "ИС", "КТП"],
     "marks": [5, 5, 5]
     }
    ]

print_students(groupmates)
print('')
sb = int(input('Введите средний балл - '))
print('')

ids = filter(groupmates, sb)

filter = []

for elem in ids:
    filter.append(groupmates[elem])

print_students(filter)
