# viewed
Application using Flask

Setup
=====

Project and Dependencies
------------------------

Mac

* $ git clone https://github.com/dnascimb/viewed.git
* $ cd viewed
* $ sudo pip install virtualenv
* $ virtualenv venv
* $ . venv/bin/activate
* $ sudo pip install Flask (or for latest) pip install https://github.com/mitsuhiko/flask/tarball/master
* $ sudo pip install sqlalchemy
* $ sudo pip install PyMySQL
* download and install mysql
* create a new local database called 'viewed' (ex. CREATE SCHEMA `viewed` DEFAULT CHARACTER SET utf8;)
* adjust the database username and password in viewed/database.py


Application Initialization
--------------------------

* $ python init_db.py
or
* $ flask --app=viewed initdb


Start the Application (Development)
-----------------------------------

* $ python runserver.py
or
* $ flask --app=viewed run
* Open a browser to http://localhost:5000/


Start the Application (Non-Development)
-----------------------------------

* edit **viewed.wsgi** appropriately
* edit **viewed.conf** appropriately
* make sure both apache and mod_wsgi are installed
* mv viewed.wsgi /var/www/viewed/
* mv viewed.conf /etc/httpd/conf.d/
* apachectl restart
* Open a browser to http://yourhost.com
