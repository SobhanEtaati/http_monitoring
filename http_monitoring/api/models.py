from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self,username ,email, password=None):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username ,email, password=None):
        return self.create_user(email ,username ,password)


class CustomUsers(AbstractUser):
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


class Urls(models.Model):
    url = models.CharField(primary_key=True, editable=False, max_length=500)
    email = models.ForeignKey(CustomUsers, on_delete = models.DO_NOTHING)
    is_successful = models.BooleanField(default=False)
    url_status_code = models.IntegerField

    if (url_status_code == 200):
        successful = True

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['email','url'], name = 'Urls_unique_value'
            )
        ]
