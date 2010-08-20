from xml.dom.minidom import parseString
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_view_exempt
import saml2sp_settings

def _get_email_from_assertion(assertion):
    """ Returns the email out of the assertion. """
    #TODO: Wrangle with XML. Ugh.
    return "dummy@dummy.com"

def _email_to_username(email):
    """
    Returns a Django-safe username based on the email address.
    This is because Django doesn't support email addresses as usernames yet.
    """
    return email.replace('@', 'AT')

def _get_user_from_assertion(assertion):
    """
    Gets info out of the assertion and locally logs in this user.
    May create a local user account first.
    Returns the user object that was created.
    """
    email = _get_email_from_assertion(assertion)
    try:
        user = User.objects.get(email = email)
    except:
        user = User.objects.create_user(
            _email_to_username(email),
            email,
            saml2sp_settings.SAML_USER_PASSWORD
        )
    #NOTE: This next line will fail if the user has changed his password
    #      via the local account. This actually is a good thing, I think.
    user = authenticate(username=user.username,
                        password=saml2sp_settings.SAML_USER_PASSWORD)
    return user

def sso_login(request):
    sso_destination = request.GET.get('next', None)
    request.session['sso_destination'] = sso_destination
    request = 'TODO'
    token = sso_destination
    tv = {
        'request_url': saml2sp_settings.IDP_REQUEST_URL,
        'request': request,
        'token': token,
        'next': sso_destination,
    }
    return render_to_response('saml2sp/sso_post_request.html', tv)

@csrf_view_exempt
def sso_response(request):
    #TODO: Only allow this view to accept POSTs from trusted sites.
    #sso_session = request.session.get('sso_destination', None),
    sso_session = request.POST.get('RelayState', None)
    data = request.POST.get('SAMLResponse', None)
    assertion = codex.decode_base64_and_inflate(data)
    user = _get_user_from_assertion(assertion)
    login(request, user)
    tv = {
        'user': user,
        'assertion': assertion,
        'sso_destination': sso_session,
    }
    return render_to_response('saml2sp/sso_complete.html', tv)

@login_required
def sso_test(request):
    tv = {
        'session': request.session,
    }
    return render_to_response('saml2sp/sso_test.html', tv)