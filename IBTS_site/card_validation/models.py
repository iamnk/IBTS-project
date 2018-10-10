from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    roll_no=models.CharField(max_length=10)
    Fee = models.CharField(max_length=10)
    rfvalue=models.CharField(max_length=20)

    def __str__(self):
        return self.roll_no

class StudentEntry(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    date=models.DateField()
