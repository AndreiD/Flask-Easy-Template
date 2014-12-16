Flask Easy-Template
========================


#### Save time on your initial setup. This is a template app that includes the most important things you'll be probably using for your flask projects.


![alt text](https://github.com/AndreiD/Flask-Easy-Template/blob/master/app/static/img/screenshot1.jpg "How the app looks 1")

You can change the theme just by replacing one word in the base.html 

![alt text](https://github.com/AndreiD/Flask-Easy-Template/blob/master/app/static/img/screenshot3.jpg "How the app looks like 2")

![alt text](https://github.com/AndreiD/Flask-Easy-Template/blob/master/app/static/img/screenshot2.jpg "How admin panel looks")


- Latest bootstrap template, modernizer, jquery etc. latest, served from content delivery networks.
- User Registry, Login & Forgot Password
- Secured Admin Panel
- REST API
- Pagination

#### How to use it:

- `git clone https://github.com/AndreiD/Flask-Easy-Template.git <project_name>` or download the zip
- `pip install -r requirements.txt`
- edit the `config.py` with your settings. (Tested with yahoo mail SMTP -> working ok)
- in **run.py** edit the port of the app (Default: 1337)
- `python run.py` -> http://server_ip:1337


optional edit `/app/templates/base.html`

> <!DOCTYPE html>
> <html lang="en" class="no-js">
> {% set bootstrap_version = '3.2.0' %}
> {% set jquery_version = '2.1.1' %}
> {% set modernizer_version = '2.8.2' %}
> {% set bootswatch_version = '3.2.0' %}
> {% set bootswatch_theme = 'slate' %}



In case a new version appears, and you want to use it. modify it. also you can chose a nice theme from http://bootswatch.com/

in __/app/models.py__ an example with "expenses list" is added.

an example with PAGINATION

##### Extras:

- a supervisord.conf [supervisor is used to monitor the web application and restart it, also starts the app in case you restart your server]
- a simple nginx.conf

Your Feedback is appreciated :)
