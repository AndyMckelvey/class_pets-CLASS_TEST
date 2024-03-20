from django.contrib import admin
from pets_for_students.models import Student, Cat


class StudentAdmin(admin.ModelAdmin):
    list_display = ('forename', 'surname', 'cat_numb')


class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'student')


admin.site.register(Student, StudentAdmin)
admin.site.register(Cat, CatAdmin)
