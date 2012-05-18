from setuptools import setup

setup(
    name = 'saml2sp',
    version = '0.14',
    author = 'John Samuel Anderson',
    author_email = 'john@andersoninnovative.com',
    description = 'SAML 2.0 SP for Django',
    long_description = 'SAML 2.0 Service Point app for Django projects.',
    install_requires = ['M2Crypto>=0.20.1'],
    license = 'MIT',
    packages = ['saml2sp', 'saml2sp.tests'],
    package_dir = {'saml2sp': 'idptest/saml2sp'},
    package_data = {'saml2sp': ['templates/saml2sp/*.html']},
    url = 'http://code.google.com/p/django-saml2-sp/',
    zip_safe = True,
)
