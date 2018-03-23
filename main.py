import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"