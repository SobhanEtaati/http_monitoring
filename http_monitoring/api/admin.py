from django.contrib import admin
from .models import CustomUsers, Urls

# Register your models here.
admin.site.register(CustomUsers)
admin.site.register(Urls)