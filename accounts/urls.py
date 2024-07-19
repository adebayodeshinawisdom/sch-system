from django.urls import path
from .views import teacher_register, student_register, teacher_dashboard, student_dashboard, CustomeLogin, CustomeLogout
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('registeration/teacher/', teacher_register, name='teacher_register'),
    path('register/student/', student_register, name='student_register'),
    path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/student/', student_dashboard, name='student_dashboard'),
    path('login/', CustomeLogin.as_view(), name='login'), 
    path('logout/', CustomeLogout, name='logout'),
]
