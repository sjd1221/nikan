from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Doctor
from .models import Personnel
from .models import Person
from django.core import serializers
import json
import pandas as pd
from django.urls import reverse
from django.http import HttpResponseRedirect





def loginpage(request):
    return render(request, "loginpage.html")


def tableshow(request, id):
    user = User.objects.filter(id = id)
    Hospital = user[0].Hospital
    doctor = Doctor.objects.raw('SELECT id, Name, Mobile, Home, [Desc], ClinicNum, ClinicAdd, IdDoctor, ClinicShift, Prof, Prof2, IMG, Hospital, HospitalExtra, Username, Password, is_active   FROM  dbo.Doctor_view_table   WHERE  Hospital = %s ', [Hospital])
    person = Person.objects.raw('SELECT  id, Name, Mobile, IdPerson, Home, About, Hospital, Username, Password, HospitalExtra, is_active   FROM  dbo.Person_view_table   WHERE  Hospital = %s ', [Hospital])
    personnel = Personnel.objects.raw('SELECT id, Name, Mobile, IdPersonnel, Home, Section, Post, Hospital, Username, Password, HospitalExtra, is_active   FROM  dbo.Personnel_view_table   WHERE  Hospital = %s ', [Hospital])
    return render(request, "viewpage.html", {
        'doctors': doctor,
        'persons': person,
        'personnels': personnel,
    })


def loginUser(request):
    Username = request.POST.get('username')
    Password = request.POST.get('password')
    user = authenticate(request, username=Username, password=Password)
    if user is not None:
        # return HttpResponse(user.Hospital)
        login(request, user)
        return redirect('nikan:tableshow', id= user.id)
    else:
        return HttpResponse("Fails")


def adddoctor(request):
    # return HttpResponse(request.GET['IdDoc'])
    if request.method == 'GET':
        IdDoc = request.GET['IdDoc']
        Doctors = Doctor.objects.filter(IdDoctor = IdDoc).all()
        serialized_data = serializers.serialize('json', Doctors)
        serialized_data = json.loads(serialized_data)
        return JsonResponse(serialized_data, safe=False)
    else:
        return HttpResponse("salam")



def removeduplicate(request):
    id = request.GET['IdDoct']
    # Doctor.objects.filter(id= id).update()

    return HttpResponse(s)
    # Hospital = user[0].Hospital
    # doctor = Doctor.objects.filter(Hospital=Hospital).all()
    # for x in doctor:
    #     Doctor.objects.filter(IdDoctor= x.IdDoctor)

    # return redirect('admin:index')