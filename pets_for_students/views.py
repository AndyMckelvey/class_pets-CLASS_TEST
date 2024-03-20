from django.shortcuts import render
from pets_for_students.models import Student, Cat


def index(request):
    student_list = Student.objects.order_by('surname')
    cat_list = Cat.objects.order_by('name')

#checks and updates cat number for students
    for student in student_list:
        student.cat_numb = Cat.objects.filter(student=student).count()
        student.save()

    context_dict = {
        'Student': student_list,
        'Cat': cat_list
    }

    return render(request, 'class_pets/index.html', context=context_dict)


def pets(request):
    cat_list = Cat.objects.order_by('name')

    context_dict = {
        'Cat': cat_list
    }

    return render(request, 'class_pets/pets.html', context=context_dict)
