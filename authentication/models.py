from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import EmailValidator


class CustomManagerModel(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email should be provided")
        email = self.normalize_email(email)
        new = self.model(email = email, **extra_fields)
        new.set_password(password)
        new.save()
        return new
    
    def create_superuser(self,email,password ,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("SuperUser is not a Staff")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("SuperUser is not a superuser(sad to say)")
        
        if extra_fields.get('is_active') is not True:
            raise ValueError("SuperUser is not a active anymore")
        
        return self.create_user(email,password,**extra_fields)
    
class User(AbstractUser):
    username = models.CharField(max_length = 25,unique = True)
    email = models.EmailField(max_length = 35,unique = True, help_text = "Add your Email", validators=[EmailValidator(message="Invalid email address.")])
    phone_number = PhoneNumberField(null=False,unique=True,help_text = "Write Phone Number")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number']


    def __str__(self):
        return f'{self.username}'
    
