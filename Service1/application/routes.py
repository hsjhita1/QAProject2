from flask import render_template
from application import app
import requests

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
    result = requests.get("http://service4:5003").text
    total = requests.get("http://service2:5001").text
    difficulty = requests.get("http://service3:5002").text
    return render_template('home.html', title = 'Home Page', result = result, total = total, difficulty = difficulty)