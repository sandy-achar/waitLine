from django.http import JsonResponse
from .models import Student, Professor, Line

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


def get_student_list(prof):
    """
    Get a list of all the students waiting in the queue for a professor.
    :param prof: Name of the professor.
    :return: String containing all the students waiting.
    """
    all_students_line = Line.objects.filter(prof_name=prof)
    students = []
    count = 1
    # Get all the student names and fill the prof object
    for i in all_students_line:
        students.append(str(count) + "." + i.student_name.student_name)
        count += 1

    return ",".join(students)


def get_prof_list():
    """
    Get a list of all the professors.
    :return: String containing all the professors.
    """
    all_profs = Professor.objects.all()
    profs = []
    # Get all the student names and fill the prof object
    for i in all_profs:
        profs.append(i.prof_name)

    return ",".join(profs)


def professors(request):
    """
    Return a list of all the professors in the system currently.
    :return: List of all the professors.
    """
    return JsonResponse({'professor': get_prof_list()})


def health_check(request):
    """
    Health check for the service.
    :return: True
    """
    return JsonResponse({'health': 'true'})


def prof_list(request, prof):
    """
    Get the JSON string of all the students for all the professors.
    :param prof_name: Name of the professor
    :return: Json string
    """
    return JsonResponse({'Professors': prof, 'Students': get_student_list(prof)})


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

    if Line.objects.filter(student_name=idiot_student, prof_name=prof_name).count() == 0:
        add_to_line = Line(student_name=idiot_student, prof_name=prof_name)
        add_to_line.save()

    return JsonResponse({'Professors': prof, 'Students': get_student_list(prof)})


def delete_from_list(request, prof, student):
    """
    Api to add student to waiting list.
    :param request: The request object.
    :return: The return object.
    """

    # Remove student from the queue.
    Line.objects.filter(student_name=student, prof_name=prof).delete()

    if Line.objects.filter(student_name=student).count() == 0:
        Student.objects.filter(student_name=student).delete()

    if Line.objects.filter(prof_name=prof).count() == 0:
        Professor.objects.filter(prof_name=prof).delete()

    return JsonResponse({'Professors': prof, 'Students': get_student_list(prof)})