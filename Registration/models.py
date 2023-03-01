from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    description = models.TextField()


class Student(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.TextField()  # name and address kena guna TextField puan cakap.
    address = models.TextField()
    phone_number = models.CharField(max_length=12)
    course_code = models.ForeignKey(
        Course, on_delete=models.CASCADE
    )  # dia akan ikut je data type primary key.
    status = models.CharField(max_length=3, default="MP")


# MP = Meneruskan Pengajian
# default value untuk kita letak terus

# kalau nak manipulate data, kena masuk dalam shell.
# python manage.py shell dia akan keluar >>> (maksudnya shell, utk database sahaja)
# add data to table. tak la susah sangat coding dia.

# masukkan 2 data dlm view

# 1. python3 manage.py shell

# 2. from Registration.models import Course
# setiap kali masuk shell, kena import semula.
# kalau nak import banyak2, just tekan from Registration.models import Course, Student
# application sahaja yg ada models, project takde.

# kalau nak save guna method save()
# 4. data.save()

# mcm mana nak tgok data selain dkt command prompt is kita tengok dalam shell.
# type nama table.objects.all().values()

# nak delete data kena guna method, so melibatkan row/object.
# mesti melibatkan .objects

# Course.objects.get(code = 'DCS').delete()
# ada 2 cara. satu display semua, satu display specific data yg kita nak (filter)

# Course .objects.all().values() display all
# Course.objects.filter(code='DCS').values()
# delete guna primary key.

# get mesti guna primary key. filter guna attribute (tapi boleh include )
# update:
# Course.objects.filter(code = 'DLH').update(description = 'Diploma in Landscape & Horticulture)
# output: 1 (means 1 data je update)
# kalau ada foreign key, cara dia lain nak tambah


# ADD DATA WITH foreign key

# dia1 = Student (id = 'DIA001', name = 'Ahmad Firdaus', address = 'Taman Batu', phone = '01110918805', course_code = a)

# 3 dcs, 1 dlh, 1 dia

# filter ikut course

#kal