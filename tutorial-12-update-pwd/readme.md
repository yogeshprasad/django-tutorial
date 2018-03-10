cd to
/Users/ykurmi/data/django/tutorial

start the server
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 manage.py runserver

Run Migrations
/Library/Frameworks/Python.framework/Versions/3.6/n/python3 manage.py migrate

Download SqlLight Browser

Update newly created tables to db
 /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 manage.py makemigrations


start mail server

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -m smtpd -n -c DebuggingServer localhost:1025


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025