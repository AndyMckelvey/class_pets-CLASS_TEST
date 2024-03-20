from django.db import models


class Student(models.Model):
    forename = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    cat_numb = models.IntegerField(default=0)

    def __str__(self):
        return self.surname


class Cat(models.Model):
    name = models.CharField(max_length=128)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
