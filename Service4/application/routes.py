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
        if score == 10:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Tripled"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money Tripled!!! ---- Score : " + total + " ----  Difficulty : " + difficulty
        elif score == 25 or score == 35 or score == 45:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Bust"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Bust! You Lose. ---- Score : " + total + " ----  Difficulty : " + difficulty
        elif score >= 40:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Double"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money doubled!! ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score >= 21:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Even"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money back ---- Score : " + total + " ----  Difficulty : " + difficulty
        elif 20 >= score:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Bust"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money lost ---- Score : " + total + " ---- Difficulty : " + difficulty
    elif difficulty == 'Medium':
        if score == 10:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Tripled"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money Tripled!!! ---- Score : " + total + " ----  Difficulty : " + difficulty
        elif score == 35 or score == 45 or score <= 30:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Bust"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Bust! You Lose. ---- Score : " + total + " ----  Difficulty : " + difficulty
        elif score > 30 and score <= 44:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Even"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money back ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score >= 45:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Double"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money doubled ---- Score : " + total + " ---- Difficulty : " + difficulty
    elif difficulty == 'Hard':
        if score == 10:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Tripled"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money Tripled!!! ---- Score : " + total + " ----  Difficulty : " + difficulty
        elif score <= 40 or score == 45:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Bust"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Bust! You Lose. ---- Score : " + total + " ----  Difficulty : " + difficulty
        elif score > 41 and score <= 49:
            addResult = results(
                board = difficulty,
                score = score,
                result = "Even"
            )
            db.session.add(addResult)
            db.session.commit()
            return "Money back ---- Score : " + total + " ---- Difficulty : " + difficulty
        elif score >= 50:
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