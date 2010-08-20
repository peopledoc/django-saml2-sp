from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from saml2sp_settings import IDP_REQUEST_URL

def sso_login(request):
    request = 'TODO'
    token = 'TODO'
    tv = {
        'request_url': IDP_REQUEST_URL,
        'request': request,
        'token': token,
    }
    return render_to_response('saml2sp/sso_post_request.html', tv)

@csrf_exempt
def sso_response(request):
    #TODO: Only allow this view to accept POSTs from trusted sites.
    tv = {}
    return render_to_response('saml2sp/sso_complete.html', tv)