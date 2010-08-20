from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from saml2sp_settings import IDP_REQUEST_URL

def sso_login(request):
    sso_destination = request.GET.get('next', None)
    request.session['sso_destination'] = sso_destination
    request = 'TODO'
    token = sso_destination
    tv = {
        'request_url': IDP_REQUEST_URL,
        'request': request,
        'token': token,
        'next': sso_destination,
    }
    return render_to_response('saml2sp/sso_post_request.html', tv)

@csrf_exempt
def sso_response(request):
    #TODO: Only allow this view to accept POSTs from trusted sites.
    #sso_session = request.session.get('sso_destination', None),
    sso_session = request.POST.get('RelayState', None)
    tv = {
        'sso_destination': sso_session,
    }
    return render_to_response('saml2sp/sso_complete.html', tv)

@login_required
def sso_test(request):
    tv = {
        'session': request.session,
    }
    return render_to_response('saml2sp/sso_test.html', tv)