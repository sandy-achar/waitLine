from django.http import JsonResponse
from .models import Student, Professor, Line
import jsonpickle

"""
I am using this as the place to create APIs. Sorry, I have used only Flask to create APIs :(.
"""


class Prof:
    """
    Class containing professors and the students waiting in line for them.
    """

    def __init__(self, prof_name):
        self.prof_name = prof_name
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)


class Return:
    """
    Class modelling the json data to be returned.
    """

    def __init__(self, professors):
        self.professors = professors


def add_to_list(request, prof, student, id):
    """
    Api to add student to waiting list.
    :param request: The request object.
    :return: The return object.
    """

    # Add student into the line.
    idiot_student = Student.objects.get_or_create(student_name=student, mav_id=id)
    prof_name = Professor.objects.get_or_create(prof_name=prof)

    idiot_student = Student.objects.get(student_name=student, mav_id=id)
    prof_name = Professor.objects.get(prof_name=prof)

    add_to_line = Line(student_name=idiot_student, prof_name=prof_name)
    add_to_line.save()

    # Get all the professors
    profs = Professor.objects.all()
    professors = []
    for i in profs:
        professors.append(Prof(i.prof_name))

    for i in professors:
        all_students_line = Line.objects.filter(prof_name=i.prof_name)

        # Get all the student names and fill the prof object
        for j in all_students_line:
            i.add_student(j.student_name)

    # Now we should have a json with all the prof-student relationship
    return_object = Return(professors)
    data = jsonpickle.encode(return_object)
    return JsonResponse(data, safe=False)
