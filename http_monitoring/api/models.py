from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self,username ,email, password=None):
        print('in CustomUserManager - create_user method')
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        # Here we hash the chosen password 
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username ,email, password=None):
        user=self.create_user(email ,username ,password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

class User(AbstractUser):
    email = models.EmailField(primary_key=True, unique=True)
    username = models.CharField(unique=True, max_length=30)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.email

