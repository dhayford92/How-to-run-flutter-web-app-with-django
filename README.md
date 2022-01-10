# How-to-run-flutter-web-app-with-django
How to run flutter web app with django server. Connecting flutter to django as one app.


first was to create django project 
And createed the flutter project in my django project

djangoproject
  | djangoproject
       | settings.py
       | urls.py
       | ...
  | flutter_web_app
  | ... 
  | other apps
  
Now edit the base tag in flutter_web_app/index.html to give the application a prefix. Note that the prefix/base should start and end with a /.

Now, in your djangoproject/urls.py, match the prefix and serve your flutter application.

To run this code
first you have to run migrate 
run django server


in browser add localhost: 194..:/flutter_web_app/
