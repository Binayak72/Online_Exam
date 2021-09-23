from django.db import models


# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=255)
    student_id = models.IntegerField()
    student_class = models.IntegerField()
    student_rollnumber = models.IntegerField()
    student_email = models.EmailField()


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=255)
    teacher_id = models.IntegerField()
    teacher_email = models.IntegerField()
    teacher_subject = models.CharField(max_length=255)
