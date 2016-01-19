from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout

try:
    from django.conf import settings
    logout_url = settings.LOGOUT_URL
    if logout_url[0] == '/':
        logout_url = logout_url[1:]
except:
    logout_url = 'accounts/logout/'

urlpatterns = [
    url(r'^' + logout_url, logout, name='logout_url'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sp/', include('sptest.saml2sp.urls')),
]
