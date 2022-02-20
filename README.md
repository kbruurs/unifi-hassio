# Unifi ticket system for Home Assistant

### Summary
A simple add-on to create tickets using the Unifi ticket system. 

Copy all files to your hassio installation in the addons folder (in a new folder called unifi_tikets). More information: https://developers.home-assistant.io/docs/add-ons/tutorial/

Step two is go to you Home assistant and go to add-ons. Click add-on store and then refresh repositories. The add-on should now show up and you should be able to install it. Fill in the configuration before starting the add-on.

The add-on is Ingress compatible so runs from wherever you're able to connect to your installation.

### Usage

Make sure to fill in the configuration with the url/ip address of your unifi controller and provide your password for the controller (or create a new user in the controller). Has been tested with v5 of the controller.

### Credits
Using: 

PyUnifi https://github.com/finish06/pyunifi

Flask https://palletsprojects.com/p/flask/

Jinja https://palletsprojects.com/p/jinja/

Gunicorn https://gunicorn.org/

NGINX https://nginx.org/

SB Admin-2 https://github.com/StartBootstrap/startbootstrap-sb-admin-2
