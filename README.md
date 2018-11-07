Flask Easy-Template
========================

## Sadly, I don't have time to maintain this. If you'd like to be a maintainer, drop me a message in an issue 

#### Save time on your initial setup. This is a template app that includes the most important things you'll be probably using for your flask projects.


You can change the theme just by replacing one word in ***base.html*** 


### Features:

- Latest bootstrap template, modernizer, jquery etc. latest, served from content delivery networks.
- User Registry, Login & Forgot Password
- Email integration with SendGrid & a contact form with recaptcha
- A sample tasks database with SQLALchemy with Pagination


#### How to use it:

- `git clone https://github.com/AndreiD/Flask-Easy-Template.git <project_name>` or download the zip
- `pip install -r requirements.txt`
- `python run.py` -> http://server_ip:5000

##### Things to do after:

- check the `config.py`
- in **run.py** edit the port of the app (Default: 5000)


For templates edit `/app/templates/base.html`

> <!DOCTYPE html>
> {% set bootstrap_version = '3.3.4' %}
> {% set jquery_version = '2.1.3' %}
> {% set modernizer_version = '2.8.3' %}
> {% set bootswatch_version = '3.3.2' %}
> {% set bootswatch_theme = 'slate' %}


In case you don't like the "slate" theme, you can chose a nice theme from http://bootswatch.com/ and just replace the theme name

Step 2. ???
Step 3. PROFIT

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

##### TROUBLESHOOTS FOR BEGINNERS :

    - READ FIRST : About Python 2 and 3 compatibility
    Some scripts and modules versions required here are written in python 2 and not ready yet for python 3 , 
    so it is recommended to download and install both interpreters python 2 and also python 3 (for windows users don't forget to add their folder paths also in your environment variables)
    Then when calling python scripts in version 2 or 3 anyway (example with the package manager script PIP), you can run default python command like :
        "python -m pip install ..." or "pip install ..."
    To call only python 3 scripts choose  this  instead :
        "py -m pip install ..." or "pip3 install ..."


    - Error parsing in requirements.txt ?
        Run instead this compatible formatted file :
            python -m pip install -r requirements-pip2.txt    
        or convert first your requirements.txt to a python 2 pip2 compatible format with this command :
            python -m pip list --format=freeze > requirements.txt


    - Error install on Proxytype : SyntaxError like Missing parentheses in call to 'print' ?
        the print function requires parentheses in Python 3 but not in Python 2 which means that the extension that you are trying to install is not yet compatible with python 3
        This is why it is recommended to install python 3 and python 2 by default.
        So run instead this compatible command for python 2 extensions (after installing python 2 if not got it yet) :
            python -m pip install -r requirements-pip2.txt
            or python -m pip install ...


    - Error install module Pycrypto : microsoft visual c++ compiler for python 2.7  is required ?
        download and install microsoft visual c++ compiler for python 2.7 here : https://www.microsoft.com/en-us/download/details.aspx?id=44266


    - Error Tornado module not found ? 
        it is a problem when installing modules like tornado in a multiple python interpreters environment 
        So run instead this common command python which precize by default  the python 2 version 
            python -m pip install -r requirements-pip2.txt
            or python -m pip install ...
            or python run.py


##### License: Apache 2.0

~~~~
Copyright 2015 AndroidAdvance.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
~~~~
limitations under the License.
