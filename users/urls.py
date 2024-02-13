from . import views
from django.urls import path, include

urlpatterns = [
    path("register/", views.register, name = "register"),
    path("authenticate/", views.authenticate_custom, name = "authenticate"),
    path('forgot-password/', views.forgot_password, name='forgot_password')
]
