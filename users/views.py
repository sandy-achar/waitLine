from django.http import JsonResponse
from .models import Student, Professor, Line


def get_student_list(prof):
    """
    All the students waiting in the queue for a professor.
    :param prof: Name of the professor.
    :return: All the students waiting.
    """
    students = []
    count = 1
    for i in Line.objects.filter(prof_name=prof):
        students.append("{}.{}".format(str(count), i.student_name.student_name))
        count += 1

    return ",".join(students)


def get_prof_list():
    """
    Get a list of all the professors.
    :return: All the professors.
    """
    profs = []
    for i in Professor.objects.all():
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
    :param prof: Name of the professor
    :return: Students waiting for the prof.
    """
    return JsonResponse({'Professors': prof, 'Students': get_student_list(prof)})


def add_to_list(request, prof, student, id):
    """
    Add a student-prof from the list.
    :param request: Request object
    :param prof: Name of professor
    :param student: Name of the student.
    :param id: Mav id of the student.
    :return: Students waiting for the prof.
    """

    # Add student into the line.
    idiot_student = Student.objects.get_or_create(student_name=student, mav_id=id)[0]
    prof_name = Professor.objects.get_or_create(prof_name=prof)[0]

    if Line.objects.filter(student_name=idiot_student, prof_name=prof_name).count() == 0:
        add_to_line = Line(student_name=idiot_student, prof_name=prof_name)
        add_to_line.save()

    return JsonResponse({'Professors': prof, 'Students': get_student_list(prof)})


def delete_from_list(request, prof, student):
    """
    Delete a student-prof from the list.
    :param request: Request object.
    :param prof: Name of professor.
    :param student: Name of the student.
    :return: Students waiting for the prof.
    """

    # Remove student from the queue.
    Line.objects.filter(student_name=student, prof_name=prof).delete()

    if Line.objects.filter(student_name=student).count() == 0:
        Student.objects.filter(student_name=student).delete()

    if Line.objects.filter(prof_name=prof).count() == 0:
        Professor.objects.filter(prof_name=prof).delete()

    return JsonResponse({'Professors': prof, 'Students': get_student_list(prof)})