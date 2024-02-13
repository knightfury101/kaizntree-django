from drf_yasg import openapi

from kaizntree_backend.Constants import (
        OAUTH_CREDENTIAL_KEY, 
        MESSAGE, 
        EMAIL, 
        NAME,
        PASSWORD, 
        ERRORS,
        ACCESS_TOKEN,
        REFRESH_TOKEN
    )

authentication_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        OAUTH_CREDENTIAL_KEY: openapi.Schema(type=openapi.TYPE_STRING)
    }
)

authentication_request_schema_201 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        MESSAGE: openapi.Schema(type=openapi.TYPE_STRING)
    }
)

authentication_request_schema_403 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
         ERRORS: openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
    }
)

authentication_custom_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        EMAIL: openapi.Schema(type=openapi.TYPE_STRING, format= openapi.FORMAT_EMAIL),
        PASSWORD: openapi.Schema(type=openapi.TYPE_STRING, format= openapi.FORMAT_PASSWORD)
    }
)

authentication_custom_schema_200 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        MESSAGE: openapi.Schema(type=openapi.TYPE_STRING),
        REFRESH_TOKEN: openapi.Schema(type = openapi.TYPE_STRING),
        ACCESS_TOKEN: openapi.Schema(type = openapi.TYPE_STRING)
    }
)

authentication_custom_schema_404 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
         ERRORS: openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
    }
)

registration_custom_schema = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties = {
        EMAIL: openapi.Schema(type=openapi.TYPE_STRING, format= openapi.FORMAT_EMAIL),
        NAME: openapi.Schema(type = openapi.TYPE_STRING),
        PASSWORD: openapi.Schema(type=openapi.TYPE_STRING, format= openapi.FORMAT_PASSWORD)
    }
)

registration_schema_201 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
         MESSAGE: openapi.Schema(type=openapi.TYPE_STRING)
    }
)

registration_schema_400 = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
         ERRORS: openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
    }
)