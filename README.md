Flask Easy-Template
========================


Save time on your initial setup. This is a skeleton app which includes the most important things you'll probably be using for most of your projects.

- Latest bootstrap template, modernizer, jquery etc. latest, served from content delivery networks.
- User Registry, Login & Forgot Password
- Secured Admin Panel
- REST API
- Pagination

How to use it:

git clone https://github.com/AndreiD/flask-easy-template.git <project_name> or download the zip
pip install -r requirements.txt
edit the "config.py" with your settings. (Tested with yahoo mail -> working ok)
in "run.py" edit the port of the app (Default: 1337)
"python run.py" -> http://server_ip:1337


in /app/templates/base.html

<!DOCTYPE html>
<html lang="en" class="no-js">
{% set bootstrap_version = '3.2.0' %}
{% set jquery_version = '2.1.1' %}
{% set modernizer_version = '2.8.2' %}
{% set bootswatch_version = '3.2.0' %}
{% set bootswatch_theme = 'slate' %}

In case a new version appears, and you want to use it. modify it. also you can chose a nice theme from http://bootswatch.com/

in /app/models.py an example with "expenses list" is added.

an example with PAGINATION

Extras:

- a supervisord.conf [supervisor is used to monitor the web application and restart it, also starts the app in case you restart your server]
- a simple nginx.conf