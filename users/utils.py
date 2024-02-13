import random

import jwt

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


from kaizntree_backend.Constants import *

def get_jwt_for_user(user):
  
    refresh = RefreshToken.for_user(user)
    refresh['user_id'] = user.id
    refresh['email'] = user.email
    refresh['name'] = user.name

    return {
        REFRESH_TOKEN: str(refresh),
        ACCESS_TOKEN: str(refresh.access_token),
    }

