from django.contrib import admin
from .models import CustomUsers, URLs

# Register your models here.
admin.site.register(CustomUsers)
admin.site.register(URLs)