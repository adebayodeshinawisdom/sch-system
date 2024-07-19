from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


# Create your models here.
class CustomerUserManager(UserManager):
    def create_superuser(self, name, email, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_superuser') is not True:
            return ValueError("user must be a superuser")
        
        if other_fields.get('is_staff') is not True:
            return ValueError("user must be a staff")
        
        return self.create_user(name, email, password, **other_fields)
    
    def create_user(self, name, email, password, **other_fields):
        if not email:
            raise ValueError("please provide a valid email")
        email = self.normalize_email(email)

        user = self.model(name=name, email=email, **other_fields)

        user.set_password(password)

        user.save()

        return user




# class User(AbstractBaseUser, PermissionsMixin):
#     name=models.CharField(max_length=255)
#     email=models.EmailField(max_length=255, unique=True)
#     passort=models.ImageField(upload_to="profile_pictures", default='default.jpg')
#     is_staff = models.BooleanField(default=False)
#     is_student= models.BooleanField(default=False)
#     is_admin=models.BooleanField(default=False)


#     REQUIRED_FIELDS = ['name']
#     USERNAME_FIELD= 'email'

#     objects= CustomerUserManager()


class User(AbstractBaseUser, PermissionsMixin):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255, unique=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    passport=models.ImageField(upload_to='user_profile')
    is_teacher=models.BooleanField(default=False)


    REQUIRED_FIELDS=['name']
    USERNAME_FIELD= 'email'

    objects = CustomerUserManager()






class TeacherProfile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ManyToManyField('Subject')
    address= models.CharField(max_length=255)
    parents=models.CharField(max_length=255)
    parents_phone=models.CharField(max_length=255)
    grade=models.ForeignKey('Grade', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.name


class Subject(models.Model):
    title = models.CharField(max_length=255)
    


class Grade(models.Model):
    title=models.CharField(max_length=255)
    
        