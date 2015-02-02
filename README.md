Flask Easy-Template
========================


#### Save time on your initial setup. This is a template app that includes the most important things you'll be probably using for your flask projects.


![alt text](https://github.com/AndreiD/Flask-Easy-Template/blob/master/app/static/img/screenshot1.jpg "How the app looks 1")

![alt text](https://github.com/AndreiD/Flask-Easy-Template/blob/master/app/static/img/screenshot3.jpg "How the app looks like 2")

You can change the theme just by replacing one word in ***base.html*** 

![alt text](https://github.com/AndreiD/Flask-Easy-Template/blob/master/app/static/img/screenshot2.jpg "How admin panel looks")


### Features:

- Latest bootstrap template, modernizer, jquery etc. latest, served from content delivery networks.
- User Registry, Login & Forgot Password
- Secured Admin Panel
- Pagination
- A sample tasks database with SQLALchemy


#### How to use it:

- `git clone https://github.com/AndreiD/Flask-Easy-Template.git <project_name>` or download the zip
- `pip install -r requirements.txt`
- `python run.py` -> http://server_ip:5000

##### Optional steps

- check the `config.py` (Tested with yahoo mail SMTP and Sendgrid SMTP -> working ok!)
- in **run.py** edit the port of the app (Default: 5000)


optional edit `/app/templates/base.html`

> <!DOCTYPE html>
> <html lang="en" class="no-js">
> {% set bootstrap_version = '3.3.2' %}
> {% set jquery_version = '2.1.3' %}
> {% set modernizer_version = '2.8.3' %}
> {% set bootswatch_version = '3.3.2' %}
> {% set bootswatch_theme = 'slate' %}


In case a new version appears, and you want to use it. modify it. also you can chose a nice theme from http://bootswatch.com/

in __/app/models.py__ an example with "expenses list" is added.

an example with PAGINATION

#### About Stars

Starring a repository allows you to keep track of projects that you find interesting, even if you aren't associated with the project.

When you star a repository, you're actually performing two distinct actions:

Creating a bookmark for easier access
**Showing appreciation to the repository maintainer for their work**

##### Extras for you:

- a supervisord.conf [supervisor is used to monitor the web application and restart it, also starts the app in case you restart your server]
- a simple nginx.conf
- after you go into production, uncomment the settings from run.py for the best performance

Your Feedback is appreciated :)

##### Last Updates:

newest first:

- updated to latest bootstrap, jquery, modernizer, bootswatch. Fixed the example sample