from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.SignupView.as_view(), name='signup'),
    path('login/', views. LoginView.as_view(), name='login')
]
