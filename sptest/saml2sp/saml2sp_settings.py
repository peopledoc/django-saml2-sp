from django.conf import settings

try:
    IDP_REQUEST_URL = settings.IDP_REQUEST_URL
except:
    IDP_REQUEST_URL = 'http://127.0.0.1:9000/idp/sso/post/request/'

#XXX: OK, this is an evil hack. But I can't figure out a better way to do this,
#     since Django requires a local user account. I suppose I could write my
#     own auth backend, but I don't really want to right now.
try:
    SAML_USER_PASSWORD = settings.SAML_USER_PASSWORD
except:
    SAML_USER_PASSWORD = settings.SECRET_KEY[::-1]