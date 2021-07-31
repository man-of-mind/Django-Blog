# Django-Blog
A blog built with django
# Matrix_capstoneProject
A blog build with django. Matrix capstone project.
## To get started fork the repo to your local system.
Open the folder using any text editor, vs code, sublime etc. or pycharm.
Ensure you have django installed on your local system.
From your terminal, make sure you are in the capstoneProject/timothyBlog/ directory.
***
Run `python manage.py runserver` 
***
Open the link shown at the output of the command above similar to `127.0.0.1:8000` on a web browser
## Admin login details
To login as the admin and have access to the django adminstration dashboard, use `username as admin and password as timothy1234`
You can change the details as you wish after you login.
### Admin Features
* Edit blog post
* Add blog post
* Delete blog post
* Like and unlike a post..😃
* Add comment
* And other default django superuser's abilities
## Registered User
You can register using the link as shown on the webpage and have access to
* Read blog post
* Like a blog post
* Unlike a blog post
* Comment on a blog post
* Read comments
## Anonymous User
An unregistered user or when not logged in, you can register or login using the link on the webpage or else, you will only be able to 
* Read post
* Read comments
* Comment on a blog post
## Making changes to the models.py file
Whenever you make a change to any of the models.py file.
Exit the server by pressing `Ctrl + C`
Then run `python manage.py makemigrations` and `python manage.py migrate`
After successful migration, run `python manage.py runserver`