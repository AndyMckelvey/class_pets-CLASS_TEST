import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'class_pets.settings')

import django

django.setup()

from pets_for_students.models import Student, Cat


def populate():
    students = {
        'Alyssa': {'for_name': 'Alyssa', 'sir_name': 'Croft'},
        'John': {'for_name': 'John', 'sir_name': 'Doe'},
        'Azam': {'for_name': 'Azam', 'sir_name': 'Khan'},
    }

    cats = [
        {'name': 'Alex', 'student': students['Alyssa']},
        {'name': 'Luna', 'student': students['Alyssa']},
        {'name': 'Mittens', 'student': students['Alyssa']},
        {'name': 'Muffins', 'student': students['John']},
        {'name': 'Jill', 'student': students['Azam']},
        {'name': 'Joe', 'student': students['Azam']},
    ]

    # Populates table
    for student, student_data in students.items():
        s = add_student(student_data['for_name'], student_data['sir_name'])
        for cat in cats:
            if cat['student'] == student_data:
                add_cat(cat['name'], s)

    # Displays Changes
    for student in Student.objects.all():
        for cat in Cat.objects.filter(student=student):
            print(f'- {cat.name}: {student.forename}')


def add_student(forename, surname, cat_numb=0):
    s = Student.objects.get_or_create(forename=forename, surname=surname)[0]
    s.forename = forename
    s.surname = surname
    s.cat_numb = cat_numb
    s.save()
    return s


def add_cat(name, student):
    c = Cat.objects.get_or_create(name=name, student=student)[0]
    c.name = name
    c.student = student
    c.save()
    return c


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population Complete')
