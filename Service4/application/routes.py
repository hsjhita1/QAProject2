from random import randint
from flask import request
from application import app

import requests

@app.route('/', methods=['GET', 'POST'])
def result():
    total = requests.get("http://service2:5001").text
    score = int(total)
    difficulty = requests.get("http://service3:5002").text
    print(score)
    print(difficulty)
    if difficulty == 'Easy':
        if score == 9:
            return "Money Tripled!!!"
        elif score == 25:
            return "Bust! You Lose."
        elif score >= 36:
            return "Money doubled!!"
        elif score >= 15:
            return "Money back"
        elif 14 >= score:
            return "Money lost"
        else:
            return "Error, please try again"
    elif difficulty == 'Medium':
        if score == 9:
            return "Money doubled"
        elif score == 25 or score <= 19:
            return "Bust. Try again"
        elif score > 20 and score <= 39:
            return "Money back"
        elif score >= 40:
            return "Money doubled"
    elif difficulty == 'Hard':
        if score == 9:
            return "Money doubled"
        elif score <= 30:
            return "Bust. Try again"
        elif score > 30 and score <= 40:
            return "Money back"
        elif score >= 41:
            return "Money doubled"