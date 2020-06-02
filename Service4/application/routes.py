from random import randint
from flask import request
from application import app

import requests

@app.route('/', methods=['GET', 'POST'])
def result():
    difficulty = requests.get("http://service3:5002").text
    total = requests.get("http://service2:5001").text
    score = int(total)

    print(score)
    print(difficulty)
    if difficulty == 'Easy':
        if score == 9:
            return "Money Tripled!!!----Score : " + total + "---- Difficulty : " + difficulty
        elif score == 25:
            return "Bust! You Lose.----Score : " + total + "---- Difficulty : " + difficulty
        elif score >= 36:
            return "Money doubled!!----Score : " + total + "----Difficulty : " + difficulty
        elif score >= 15:
            return "Money back----Score : " + total + "---- Difficulty : " + difficulty
        elif 14 >= score:
            return "Money lost----Score : " + total + "----Difficulty : " + difficulty
        else:
            return "Error, please try again"
    elif difficulty == 'Medium':
        if score == 9:
            return "Money doubled----Score : " + total + "----Difficulty : " + difficulty
        elif score == 25 or score <= 19:
            return "Bust. Try again----Score : " + total + "----Difficulty : " + difficulty
        elif score > 20 and score <= 39:
            return "Money back----Score : " + total + "----Difficulty : " + difficulty
        elif score >= 40:
            return "Money doubled----Score : " + total + "----Difficulty : " + difficulty
    elif difficulty == 'Hard':
        if score == 9:
            return "Money doubled----Score : " + total + "----Difficulty : " + difficulty
        elif score <= 30:
            return "Bust. Try again----Score : " + total + "----Difficulty : " + difficulty
        elif score > 30 and score <= 40:
            return "Money back----Score : " + total + "----Difficulty : " + difficulty
        elif score >= 41:
            return "Money doubled----Score : " + total + "----Difficulty : " + difficulty