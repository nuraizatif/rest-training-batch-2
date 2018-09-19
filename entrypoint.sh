#!/usr/bin/env bash

######## part 1 - install virtualenv & flask
pip install virtualenv
virtualenv -p /usr/local/bin/python3.6 env_p36
cd env_p36
### start : this section need to run manually inside container
# source bin/activate
# pip install flask flask-restful
# touch requirements.txt
# pip freeze > requirements.txt
### end

# python api.py

# only sleep for 24 hours, fo triggering container
howlong=$((24*3600))
sleep $howlong
