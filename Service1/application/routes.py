from flask import render_template
from application import app
import requests

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
    result = requests.get("http://service4:5003").text
    print(result)
    return render_template('home.html', title = 'Home Page', result = result)