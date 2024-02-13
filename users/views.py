from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions

from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from kaizntree_backend.Constants import *
from kaizntree_backend.status_codes import STATUS

from .utils import get_jwt_for_user
from .schemas import *
from .models import *
from .serializers import CustomUserSerializer, ForgotPasswordSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.utils.encoding import force_bytes

@swagger_auto_schema(method='post', 
                     operation_description = "Register new user in database", 
                     request_body = registration_custom_schema, 
                     responses = {201:registration_schema_201,
                                  400:registration_schema_400},
                     tags = [AUTHENTICATE] )
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    custom_user_serializer = CustomUserSerializer(data=request.data)
    if not custom_user_serializer.is_valid():
        return Response(custom_user_serializer.errors, status = STATUS[400])
    user = custom_user_serializer.save()
    user.set_password(request.data['password'])
    user.save()
    data = {
        MESSAGE: "User Registered", 
        USER: custom_user_serializer.data
    }
    return Response(data = data, status = STATUS[201])

@swagger_auto_schema(method='post', 
                     operation_description = "Authenticate user with custom credentials", 
                     request_body=authentication_custom_schema, 
                     responses = {200:authentication_custom_schema_200,
                                  404:authentication_custom_schema_404},
                     tags = [AUTHENTICATE])
@api_view(['POST'])
def authenticate_custom(request):
    user = CustomUser.objects.get(email = request.data["email"])
    
    if user is None:
        data = {
            ERROR: "User does not exist"
        }
        return Response(data, status = STATUS[404])
    
    user_ = authenticate(request, username= request.data["email"], password=request.data["password"])
    if user_ is not None:
        token = get_jwt_for_user(user_)
        data = {
            MESSAGE: "User Authenticated",
            
        }
        data = dict(data, **token)
        return Response(data, status= STATUS[200])
    else:
        data = {
            ERROR: "Could not authenticate"
        }
        # No backend authenticated the credentials
        return Response(data, status = STATUS[404])


@swagger_auto_schema(method='post', 
                     operation_description = "Reset Password for Authenticated Users", 
                     request_body=ForgotPasswordSerializer, 
                     tags = [AUTHENTICATE])    
    
@api_view(['POST'])
def forgot_password(request):
    if request.method == 'POST':
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User with this email does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            # Generate a password reset token
            token = default_token_generator.make_token(user)

            # Encode the user's primary key and token to be sent in the email
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Send password reset email to the user
            reset_url = f'http://example.com/reset-password/{uid}/{token}/'
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_url}',
                'adityasingh.gmu@gmail.com',
                [email],
                fail_silently=False,
            )

            # Return success response
            return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)