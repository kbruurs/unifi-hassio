#!/usr/bin/with-contenv bashio
declare ingress_entry
ingress_entry=$(bashio::addon.ingress_entry)

sed -i "s#%%ingress_entry%%#${ingress_entry}#g" /unifiticket.py

echo Starting gunicorn server
gunicorn --bind 0.0.0.0:8765 wsgi:app