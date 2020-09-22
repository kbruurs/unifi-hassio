#!/usr/bin/with-contenv bashio

bashio::log.info $(bashio::addon.ingress_entry)

declare ingress_entry
ingress_entry=$(bashio::addon.ingress_entry)

sed -i "s#%%ingress_entry%%#${ingress_entry}#g" /etc/nginx/nginx.conf
