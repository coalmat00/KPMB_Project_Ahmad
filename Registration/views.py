from django.shortcuts import render
from Registration.models import Course, Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):

    """context = {
        coursecode:
    }"""
    return render(request, "index.html")


def new_course(request):
    if request.method == "POST":
        c_code = request.POST["code"]  # kita ambik dari input nama code
        c_desc = request.POST["description"]  # kita ambik dari input nama desc
        data = Course(code=c_code, description=c_desc)
        data.save()
        dict = {"message": "Data saved."}  # utk hantar message sahaja.

    elif request.method == "DELETE":
        c_code = request.DELETE["code"]  # kita ambik dari input nama code
        data = Course.objects.get(code=c_code)
        data.delete()
        data.save()
        dict = {"message": "Data deleted."}

    else:
        dict = {"message": ""}
    return render(request, "new_course.html", dict)


def new_student(request):
    allcourse = Course.objects.all()
    dict = {}
    # declare the variable before the if statement
    if request.method == "POST":
        s_id = request.POST["id"]
        s_name = request.POST["name"]
        s_address = request.POST["address"]
        s_phone_number = request.POST["phone_number"]
        s_course = request.POST["s_course"]
        s_code = Course.objects.get(code=s_course)
        data = Student(
            id=s_id,
            name=s_name,
            address=s_address,
            phone_number=s_phone_number,
            course_code=s_code,
        )
        data.save()
        dict = {"allcourse": allcourse, "message": "Student data is saved."}

        # update the value of the variable
    else:  # maksudnya sebelum dia save.
        dict = {"allcourse": allcourse}

    return render(request, "new_student.html", dict)


def search_by_course(request):
    allcourse = Course.objects.all()
    student = Student.objects.all()
    if request.method == "GET":
        student = Student.objects.filter(course_code=request.GET.get("s_course"))
        number = len(student)
        dict = {
            "number": number,
            "student": student,
            "allcourse": allcourse,
            "message": "Searched and displayed.",
            "course": request.GET.get("s_course"),
        }

    else:
        dict = {"allcourse": allcourse}
    return render(request, "search_by_course.html", dict)


def course(request):
    allcourse = Course.objects.all()
    dict = {"allcourse": allcourse}  # pass data kepada html mesti melalui dictionary.
    return render(
        request, "course.html", dict
    )  # letak dict as 2nd parameter so that nanti dia render sekali data.


def search_course(request):
    if request.method == "GET":
        data = Course.objects.filter(code=request.GET.get("c_code"))
        dict = {"data": data}

        return render(request, "search_course.html", dict)
    else:
        return render(request, "search_course.html")


def update_course(request, code):
    data = Course.objects.get(code=code)
    dict = {"data": data}
    return render(request, "update_course.html", dict)


def save_update_course(request, code):
    c_desc = request.POST["desc"]  # yg ni kena square bracket
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))


# render: to load / up.
