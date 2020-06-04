from flask import render_template
from application import app, db
from application.models import results
import requests

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
    resultsData = results.query.all()
    result = requests.get("http://service4:8003").text
    print(result)
    return render_template('home.html', title = 'Home Page', result = result, data1 = resultsData)