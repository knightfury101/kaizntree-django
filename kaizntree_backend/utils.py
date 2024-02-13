from datetime import datetime, timedelta
import calendar

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status

from .status_codes import STATUS
from .Constants import *

schema_view = get_schema_view(
   openapi.Info(
      title="Kaizntree Backend",
      default_version='v1',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="adityasingh.gmu@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

def create_error_message_response(message, status = STATUS[400]):
   data = {
      ERROR: message
   }

   return Response(data, status)

def get_today_date():
   current_date = datetime.today()

   return current_date

def get_other_date(num_days, current_date = get_today_date(), prev = False):
   days = timedelta(num_days)
   
   if isinstance(current_date, str):
      current_date = datetime.strptime(current_date, "%Y-%m-%d")

   other_date = current_date - days if prev else current_date + days

   return other_date

def get_other_date_string(num_days, current_date = get_today_date(), prev = False):
   other_date = get_other_date(num_days, current_date, prev)

   other_date = datetime.strftime(other_date, "%Y-%m-%d")

   return other_date

def get_current_month():
   return datetime.now().month

def get_current_year():
   return datetime.now().year

def get_dates(year, month):
   import datetime
   num_days = calendar.monthrange(year, month)[1]
   days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]

   return days

def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m