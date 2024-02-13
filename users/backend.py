from django.contrib.auth.hashers import check_password 

from .models import CustomUser

class CustomUserBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            # Try to find a user matching your username
            user = CustomUser.objects.get(username=username)

            #  Check the password is the reverse of the username
            if check_password(password, user.password):
                # Yes? return the Django user object
                return user
            else:
                # No? return None - triggers default login failed
                return None
        except CustomUser.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None