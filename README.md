# HPDF-week1
Contains all the tasks assigned to me durning week1 of the internship at hasura
# Installation
Download python from https://www.python.org/downloads/ and select the most appropriate version (I have used python 3.5 for this project)  and install it. You will also need flask and virtualenv so to install them open your command prompt and change the directory by cd command to ../Script folder of python and type pip install flask/virtualenv and press enter.
# Week1 Tasks
## Task 1
###### A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"; replace "Arpit" with your own     first name).
First we imported the Flask class. An instance of this class will be our WSGI application.Next we create an instance of this class. The first argument is the name of the application’s module or package.This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.We then use the route() decorator to tell Flask what URL should trigger our function.The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.Save the file with some name(hello.py) and to execute it write export FLASK_APP=hello.py
and flask run in cmd.

## Task 2
###### Add a route, for e.g. http://localhost:8080/authors, which:
###### a) fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
###### b) fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
###### c) Respond with only a list of authors and the count of their posts (a newline for each author).
We first create a route /authors and define authors().We need to use requests() for which we need to import request.We create two response objects to fetch the data from the given URL by using requests.get() and then parse it using json().Finally we render a HTML page it using render_template() where we pass 3 arguments : page_name.html,var_name1,var_name2) where var_name1,var_name2 contains parsed json() data.
In authors.html (which i have used in my project) we create 2 loops : one for authors and another for posts. Whenever Ids of both matches then we increament the post written by that author.Execute the file similar to task1 as explained above 

## Task 3
###### Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-
Add a route /setcookie and define the function setcookie().Make a response object and display some text which will be helpful for us to know that our code is wrking. Using set_cookie() we set two cookies one with our name and another with our age and then return the response object.

## Task 4
###### Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.
Add a route /getcookie and define the function getcookie() which contains two variables that fetches data from cookies using request.cookies.get('cookie_name').Import request for this function and return the output.

## Task 5
###### Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)
Add a route /robots.txt and define function deny().Import abort to use abort() and pass 401 as arguments which represents error number.

## Task 6
###### Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.
As we have used render_template() in /authors(Task 2) similarly we return it using the same function and pass page_name.html as arguments

## Task 7
###### A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received to stdout.
First we create a /input route which renders a HTML page containing a textbox and submit button.In action attribute the the form we define "/display" and method as POST.We recieve the value submitted by user on /input by using request.form and print the output.


 
