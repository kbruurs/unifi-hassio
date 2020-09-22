#!/usr/bin/with-contenv bashio
declare ingress_entry
ingress_entry=$(bashio::addon.ingress_entry)

sed -i "s#%%ingress_entry%%#${ingress_entry}#g" /hello.py

echo Starting http server
export FLASK_APP=hello.py
flask run --host=0.0.0.0 --port=8765
