# Python imports
import base64
from xml.dom.minidom import parseString
# Django imports
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_view_exempt
# Local imports
import base
import codex
import saml2sp_settings
import xml_render


#TODO: Pull IDP choices from a model. For now, just use the one from the settings.
IDP_CHOICES = (
    (saml2sp_settings.SAML2SP_IDP_REQUEST_URL,
     saml2sp_settings.SAML2SP_IDP_REQUEST_URL),
)
class IdpSelectionForm(forms.Form):
    idp = forms.ChoiceField(choices=IDP_CHOICES)

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
        user = User.objects.get(email=email)
    except:
        user = User.objects.create_user(
            _email_to_username(email),
            email,
            saml2sp_settings.SAML2SP_SAML_USER_PASSWORD
        )
    #NOTE: This next line will fail if the user has changed his password
    #      via the local account. This actually is a good thing, I think.
    user = authenticate(username=user.username,
                        password=saml2sp_settings.SAML2SP_SAML_USER_PASSWORD)
    return user

def sso_login(request, request_url):
    """
    Replies with an XHTML SSO Request.
    """
    sso_destination = request.GET.get('next', None)
    request.session['sso_destination'] = sso_destination
    parameters = {
        'ACS_URL': saml2sp_settings.SAML2SP_ACS_URL,
        'DESTINATION': sso_destination,
        'AUTHN_REQUEST_ID': base.get_random_id(),
        'ISSUE_INSTANT': base.get_time_string(),
        'ISSUER': saml2sp_settings.SAML2SP_ACS_URL,
    }
    authn_req = xml_render.get_authnrequest_xml(parameters, signed=False)
    request = base64.b64encode(authn_req)
    token = sso_destination
    tv = {
        'request_url': request_url, #saml2sp_settings.IDP_REQUEST_URL,
        'request': request,
        'token': token,
        'next': sso_destination,
    }
    return render_to_response('saml2sp/sso_post_request.html', tv)

def sso_idp_select(request):
    """
    Allows the user to select an IDP.
    """
    if request.method == 'POST':
        form = IdpSelectionForm(request.POST)
        if form.is_valid():
            idp_request_url = form.cleaned_data['idp']
            return sso_login(request, idp_request_url)
    else:
        form = IdpSelectionForm()
    tv = {
        'form': form,
    }
    return render_to_response('saml2sp/sso_idp_selection.html', tv,
        context_instance=RequestContext(request))


@csrf_view_exempt
def sso_response(request):
    """
    Handles a POSTed SSO Assertion and logs the user in.
    """
    #TODO: Only allow this view to accept POSTs from trusted sites.
    #sso_session = request.session.get('sso_destination', None),
    sso_session = request.POST.get('RelayState', None)
    data = request.POST.get('SAMLResponse', None)
    assertion = codex.decode_base64_and_inflate(data)
    #TODO: Expand this next bit to process/translate attributes, too:
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
    """
    Exposes a simple resource that requires authentication,
    so that we can kick-off the SAML conversation.
    """
    tv = {
        'session': request.session,
    }
    return render_to_response('saml2sp/sso_test.html', tv)
