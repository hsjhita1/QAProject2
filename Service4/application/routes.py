from random import randint
from flask import request
from application import app, db
from application.models import results

import requests

@app.route('/', methods=['GET', 'POST'])
def result():
    difficulty = requests.get("http://service3:8002").text
    total = requests.get("http://service2:8001").text
    score = int(total)
    if difficulty == 'Easy':
        if score == 10 or score >= 51:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Tripled"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money Tripled!!! ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score <= 30:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Bust"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Bust! You Lose. ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score >= 41:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Double"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money doubled!! ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score >= 31:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Even"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money back ---- Score : " + total + " ---- Difficulty : " + difficulty
    elif difficulty == 'Medium':
        if score == 10 or score >= 56:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Tripled"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money Tripled!!! ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score <= 35:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Bust"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Bust! You Lose. ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score > 35 and score <= 45:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Even"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money back ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score >= 46:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Double"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money doubled ---- Score : " + total + " ---- Difficulty : " + difficulty
    elif difficulty == 'Hard':
        if score == 10 or score >= 56:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Tripled"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money Tripled!!! ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score <= 40:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Bust"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Bust! You Lose. ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score > 41 and score <= 50:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Even"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money back ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score >= 51:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Double"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money doubled ---- Score : " + total + " ---- Difficulty : " + difficulty
    else:
        return "Error, please try again"