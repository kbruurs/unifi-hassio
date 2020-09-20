#!/usr/bin/with-contenv bashio

echo Starting http server
export FLASK_APP=hello.py
flask run -h 0.0.0.0 -p 8765
