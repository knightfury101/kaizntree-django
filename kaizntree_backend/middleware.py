from django.contrib.auth.middleware import get_user
from django.utils.functional import SimpleLazyObject

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .Constants import *

EXCLUDE_FROM_MIDDLEWARE = ['/users/authenticate/', '/users/register/']

class JSONAuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        request.user = SimpleLazyObject(lambda:self.__class__.get_jwt_user(request))
        
        print("jwt auth", request.user)
        return self.get_response(request)
    

    @staticmethod
    def get_jwt_user(request):
        user = get_user(request)
        
        if user.is_authenticated:
            return user
        jwt_authentication = JWTAuthentication()
        if jwt_authentication.get_header(request):
            user, jwt = jwt_authentication.authenticate(request)
        return user

class AuthorizationMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        view_name = '.'.join((view_func.__module__, view_func.__name__))
        print("process view auth")
        if view_name in EXCLUDE_FROM_MIDDLEWARE:
            return None

    def __call__(self, request):
        token = request.headers.get("Http-Authorization")
        if token:
            request.META[AUTHENTICATION_HEADER] = f'{token}'
        return self.get_response(request)