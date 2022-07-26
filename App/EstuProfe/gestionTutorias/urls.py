from django.urls import path
from gestionTutorias import views

urlpatterns = [
    path('login/', views.loginPage, name="LoginPage"),
    path('register/', views.registerPage, name="RegisterPage"),
    path('interest/',views.interestPage, name="InterestPage"),
    path('student/', views.studentPage, name="StudentPage"),
    path('tutor/', views.tutorPage, name="TutorPage"),
]