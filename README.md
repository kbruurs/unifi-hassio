# Unifi ticket system for Home Assistant

### Summary
A simple add-on to create tickets using the Unifi ticket system. 

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