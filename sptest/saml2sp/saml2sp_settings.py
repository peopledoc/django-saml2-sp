from django.conf import settings

#TODO: Standardize these settings like the SAML2 settings are.
try:
    ACS_URL = settings.ACS_URL
except:
    ACS_URL = 'http://127.0.0.1:9000/sp/acs/'

try:
    SLO_URL = settings.SLO_URL
except:
    SLO_URL = 'http://127.0.0.1:8000/idp/logout/'

try:
    IDP_REQUEST_URL = settings.IDP_REQUEST_URL
except:
    IDP_REQUEST_URL = 'http://127.0.0.1:8000/idp/login/'

#XXX: OK, this is an evil hack. But I can't figure out a better way to do this,
#     since Django requires a local user account. I suppose I could write my
#     own auth backend, but I don't really want to right now.
try:
    SAML_USER_PASSWORD = settings.SAML_USER_PASSWORD
except:
    SAML_USER_PASSWORD = settings.SECRET_KEY[::-1]

# If using relative paths, be careful!
try:
    SAML2IDP_CERTIFICATE_FILE = settings.SAML2IDP_CERTIFICATE_FILE
except:
    SAML2IDP_CERTIFICATE_FILE = 'keys/certificate.pem'

# If using relative paths, be careful!
try:
    SAML2SP_PRIVATE_KEY_FILE = settings.SAML2IDP_PRIVATE_KEY_FILE
except:
    SAML2SP_PRIVATE_KEY_FILE = 'keys/private-key.pem'
