from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import TeacherRegistrationForm, StudentRegistrationForm
from .decorators import teacher_required, student_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout

#logout function
def CustomeLogout(request):
    logout(request)
    return redirect(reverse_lazy('login'))
    
#login function
class CustomeLogin(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_teacher:
            return reverse_lazy('teacher_dashboard')
        elif user.is_student:
            return reverse_lazy('student_dashboard')
        
        else:
            return reverse_lazy('login')




#View function for registring a teacher
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher_dashboard')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


#view function for registring a student
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})





@teacher_required
def teacher_dashboard(request):
    return render(request, 'dashboard/teacher_dashboard.html')

@student_required
def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')
