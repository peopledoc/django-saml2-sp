#!/bin/bash
# Hudson CI Test Script - for Linux
pushd .
cd sptest
echo Testing in directory: `pwd`
echo `python -V`
echo Django Version: `python manage.py --version`
# Only test our apps, not the Django core apps:
python manage.py test saml2sp
popd
