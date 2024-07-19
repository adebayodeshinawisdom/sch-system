from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, TeacherProfile, StudentProfile, Subject, Grade


#Teacher Registration form

class TeacherRegistrationForm(UserCreationForm):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    grade = forms.ModelChoiceField(queryset=Grade.objects.all())
    address=forms.CharField()
    phone_number=forms.CharField()

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
            TeacherProfile.objects.create(
                user=user,
                subject=self.cleaned_data['subject'],
                grade=self.cleaned_data['grade'],
                address=self.cleaned_data['address'],
                phone_number=self.cleaned_data['phone_number']
            )
        return user
    

    #student registration form
class StudentRegistrationForm(UserCreationForm):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
    grade = forms.ModelChoiceField(queryset=Grade.objects.all())
    parents=forms.CharField(max_length=255)
    parents_phone=forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
            student_profile = StudentProfile.objects.create(
                user=user,
                grade=self.cleaned_data['grade'],
                address=self.cleaned_data['address'],
                parents=self.cleaned_data['parents'],
                parents_phone=self.cleaned_data['parents_phone']
            )
            student_profile.subjects.set(self.cleaned_data['subjects'])
        return user
