from flask import render_template
from application import app

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home Page')