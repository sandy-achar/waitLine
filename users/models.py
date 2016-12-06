from django.db import models


class Professor(models.Model):
    """
    Class modelling the professors available for consultation.
    """
    prof_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.prof_name


class Student(models.Model):
    """
    Class modelling the students waiting in line.
    """
    student_name = models.CharField(max_length=50, unique=True)
    mav_id = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name


class Line(models.Model):
    """
    Class modelling the wait line.
    """
    position = models.AutoField(primary_key=True)
    student_name = models.ForeignKey(Student, to_field='student_name')
    prof_name = models.ForeignKey(Professor, to_field='prof_name')

    def __str__(self):
        return str(self.position) + " - " + str(self.prof_name) + " : " + str(self.student_name)
