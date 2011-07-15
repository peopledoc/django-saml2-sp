#!/bin/bash
# Hudson CI Test Script - for Linux
pushd .
cd sptest
pwd
python manage.py test
popd
