import email
from django.shortcuts import render, HttpResponse
from gestionTutorias.forms import LoginForm
from gestionTutorias.models import Users

def login(request):
    if request.method=="POST":
        print("SI IMPRIME")
        login = LoginForm(request.POST)
        if login.is_valid():
            infoLogin = login.cleaned_data

            lg = Users.objects.filter(email__icontains=infoLogin['email'], password__icontains = infoLogin['password'], type_icontains = infoLogin['type'])
            if lg.count == 1:
                print("SI TIENE 1")
                return render(request, "gestionTutorias/home_student.html")
            else:
                print("NO TIENE 1")
                return render(request, "gestionTutorias/login.html")
            
    else:
        print("NI ENTRA")
        login = LoginForm()
        return render(request, "gestionTutorias/login.html")

def loginPage(request):
    return render(request, "gestionTutorias/login.html")

def registerPage(request):
    return render(request, "gestionTutorias/register.html")

def interestPage(request):
    return render(request, "gestionTutorias/interest_area.html")

def studentPage(request):
    return render(request, "gestionTutorias/home_student.html")

def tutorPage(request):
    return render(request, "gestionTutorias/home_tutor.html")