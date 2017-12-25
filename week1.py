import requests,sys
from flask import Flask,abort
from flask import render_template,request,make_response,redirect

app = Flask(__name__)

#A simple hello-world at http://localhost:8080/ that displays a simple string 
@app.route('/')
def index():
	return "Hello World - Parth"

#Add a route, for e.g. http://localhost:8080/authors, which: fetches 2 list from different URL and display a list of authors and the count of their posts
@app.route("/authors")
def authors():
	resp = requests.get('https://jsonplaceholder.typicode.com/users/')
	response = requests.get('https://jsonplaceholder.typicode.com/posts')
	users = resp.json()
	posts = response.json()
	return render_template('authors.html',authors=users,posts=posts)

#Set a simple cookie
@app.route("/setcookie")
def settcookie():
	resp = make_response('Setting Cookie')
	resp.set_cookie('name' , 'Parth Panchal')
	resp.set_cookie('age' , '20')
	return resp 
	return '';

#Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.
@app.route("/getcookie")
def getcookie():
	name = request.cookies.get('name')
	age = request.cookies.get('age')
	return 'The name is ' +name + ' and age is ' +age;

#Deny requests to your http://localhost:8080/robots.txt page.
@app.route("/robots.txt")
def deny():
	return abort(401)

#Render an HTML page at http://localhost:8080/html or an image
@app.route('/html')
def html():
    return(render_template('test.html'))

#A text box at http://localhost:8080/input which sends the data as POST to any endpoint.
@app.route('/input')
def input():
    return(render_template('input.html'))

#This endpoint should log the received the received to stdout.	
@app.route('/display', methods = ['POST', 'GET'])
def display():
   if request.method == 'POST':
       user = request.form['post']
       print(user, file=sys.stdout)
   return 'Output is displayed on terminal ' +user

#to run the app
if __name__ == '__main__':
	app.run(debug=True)