from django.shortcuts import render_to_response

def sso_login(request):
    tv = {}
    return render_to_response('saml2sp/sso_login.html', tv)
