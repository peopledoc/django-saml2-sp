from django.conf import settings

try:
    IDP_REQUEST_URL = settings.IDP_REQUEST_URL
except:
    IDP_REQUEST_URL = 'http://127.0.0.1:9000/idp/sso/post/request/'