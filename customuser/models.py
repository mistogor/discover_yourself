from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, phone_number, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, phone_number, gender, password=None):
        user = self.create_user(
            email=email,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            gender=gender,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    name = models.CharField(max_length=64)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    date_of_birth = models.DateField(verbose_name='date of birth', null=True)
    phone_number = models.CharField(verbose_name='phone number', max_length=15, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'phone_number', 'gender']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
