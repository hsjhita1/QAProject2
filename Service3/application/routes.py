import random
import requests
from application import app

@app.route('/', methods=['GET', 'POST'])
def scoring():
    scoring = ['Easy', 'Medium', 'Hard']
    return scoring[random.randrange(len(scoring))]