from django.db import models


class Professor(models.Model):
    """
    Class modelling the professors available for consultation.
    """
    prof_id = models.AutoField(primary_key=True)
    # Enter the full name of the professor
    prof_name = models.CharField(max_length=50)

    def __str__(self):
        return self.prof_name


class Student(models.Model):
    """
    Class modelling the students waiting in line.
    """
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    mav_id = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name


class Line(models.Model):
    """
    Class modelling the wait line.
    """
    position = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, to_field='student_id')
    prof_id = models.ForeignKey(Professor, to_field='prof_id')

    def __str__(self):
        return str(self.position) + " - " + str(self.prof_id) + " : " + str(self.student_id)
