# flask-API

A simple API built with Python and flask.<br>
It has three endpoints:<br>
1.) / which displays a small documentation<br>
2.) /sum to sum two numbers<br>
3.) /mult to multiply two numbers<br>
<br>
Example call: localhost:5000/sum?a=5&b=3<br>

## Prerequisites
Python 3.8<br>
flask<br>
docker<br>

## Docker commands
1.) docker build -t flask_api:latest<br>
2.) docker run -d -p 5000:5000 --name=api flask_api<br>

## Youtube Video Tutorial
https://www.youtube.com/watch?v=Poopo_K21Kw
