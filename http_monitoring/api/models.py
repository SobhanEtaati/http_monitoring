from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The username field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        return self.create_user(email, username, password)


class CustomUsers(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True ,unique=True)
    username = models.CharField(primary_key=True ,max_length=30, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        constrains = [
            models.UniqueConstraint(
                fields=['email', 'username'], name = 'CustomUsers_primary_key'
            )
        ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class URLs(models.Model):
    username = models.ForeignKey(CustomUsers.username)
    url = models.CharField(primary_key=True, editable=False)
    successful = models.BooleanField(default=False)
    status_code = models.IntegerField
    if (status_code == 200):
        successful = True

    class Meta:
        constrains = [
            models.UniqueConstraint(
            fields=['username','url'], name = 'URLs_primary_key'
            )
        ]
