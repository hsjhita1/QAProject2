from application import db
from datetime import datetime

class results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String(10), nullable = False)
    score = db.Column(db.Integer, nullable = False)
    result = db.Column(db.String(20), nullable = False)
    date_played = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)