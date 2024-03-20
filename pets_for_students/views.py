from django.shortcuts import render
from pets_for_students.models import Student, Cat


def index(request):

    student_list = Student.objects.order_by('surname')

    for student in student_list:
        student.cat_numb = Cat.objects.filter(student=student).count()
        student.save()

    cat_list = Cat.objects.order_by('name')

    context_dict = {}
    context_dict['Student'] = student_list
    context_dict['Cat'] = cat_list

    # Render the response and send it back!
    return render(request, 'class_pets/index.html', context=context_dict)