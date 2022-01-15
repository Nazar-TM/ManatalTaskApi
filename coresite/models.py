from django.db import models


# models code goes here
class School(models.Model):
    school_name = models.CharField(max_length=20, help_text="valid school name")
    no_of_students = models.IntegerField(help_text="number of students")
    location = models.CharField(max_length=50, help_text="school locations")

    def __str__(self):
        return self.school_name


class Student(models.Model):
    student_id = models.ForeignKey(School, on_delete=models.CASCADE, help_text="student id belongs to school")
    first_name = models.CharField(max_length=20, help_text="please enter first name")
    last_name = models.CharField(max_length=20, help_text="please enter last name")

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)
