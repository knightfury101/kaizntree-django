from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from kaizntree_backend.Constants import *
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length = 25, null = True, blank = True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @classmethod
    def create_user_from_request(cls, request):
        email = request.data.get(EMAIL)
        name = request.data.get(NAME)
        
        return cls.objects.create(email = email, name = name)
    
    @classmethod
    def get_user_from_request(cls, request):
        user = request.user
        custom_user = None

        try:
            custom_user = CustomUser.objects.get(email = user.email)
        except Exception as e:
            print(e)

        return custom_user