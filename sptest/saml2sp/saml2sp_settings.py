from django.conf import settings

try:
    SAML2SP_ACS_URL = settings.SAML2SP_ACS_URL
except:
    SAML2SP_ACS_URL = 'http://127.0.0.1:9000/sp/acs/'

try:
    SAML2SP_SLO_URL = settings.SAML2SP_SLO_URL
except:
    SAML2SP_SLO_URL = 'http://127.0.0.1:8000/idp/logout/'

try:
    SAML2SP_IDP_REQUEST_URL = settings.SAML2SP_IDP_REQUEST_URL
except:
    SAML2SP_IDP_REQUEST_URL = 'http://127.0.0.1:8000/idp/login/'

#XXX: OK, this is an evil hack. But I can't figure out a better way to do this,
#     since Django requires a local user account. I suppose I could write my
#     own auth backend, but I don't really want to right now.
try:
    SAML2SP_SAML_USER_PASSWORD = settings.SAML2SP_SAML_USER_PASSWORD
except:
    SAML2SP_SAML_USER_PASSWORD = settings.SECRET_KEY[::-1]

# If using relative paths, be careful!
try:
    SAML2SP_CERTIFICATE_FILE = settings.SAML2SP_CERTIFICATE_FILE
except:
    SAML2SP_CERTIFICATE_FILE = 'keys/certificate.pem'

# If using relative paths, be careful!
try:
    SAML2SP_PRIVATE_KEY_FILE = settings.SAML2SP_PRIVATE_KEY_FILE
except:
    SAML2SP_PRIVATE_KEY_FILE = 'keys/private-key.pem'
