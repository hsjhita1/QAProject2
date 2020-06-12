import pytest, unittest, requests, flask
from unittest.mock import patch
from application import app, db, routes
from application.models import results
from flask import url_for
from flask_testing import TestCase
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        config_name = 'test'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
            DEBUG=True
        )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):    
    def test_easy(self):
        assert routes.result('Easy', '10') == "Money Tripled!!! ---- Score : 10 ---- Difficulty : Easy"
        assert routes.result('Easy', '30') == "Bust! You Lose. ---- Score : 30 ---- Difficulty : Easy"
        assert routes.result('Easy', '45') == "Money doubled!! ---- Score : 45 ---- Difficulty : Easy"
        assert routes.result('Easy', '35') == "Money back ---- Score : 35 ---- Difficulty : Easy"

    def test_medium(self):
        assert routes.result('Medium', '10') == "Money Tripled!!! ---- Score : 10 ---- Difficulty : Medium"
        assert routes.result('Medium', '35') == "Bust! You Lose. ---- Score : 35 ---- Difficulty : Medium"
        assert routes.result('Medium', '36') == "Money back ---- Score : 36 ---- Difficulty : Medium"
        assert routes.result('Medium', '47') == "Money doubled ---- Score : 47 ---- Difficulty : Medium"

    def test_hard(self):
        assert routes.result('Hard', '10') == "Money Tripled!!! ---- Score : 10 ---- Difficulty : Hard"
        assert routes.result('Hard', '40') == "Bust! You Lose. ---- Score : 40 ---- Difficulty : Hard"
        assert routes.result('Hard', '45') == "Money back ---- Score : 45 ---- Difficulty : Hard"
        assert routes.result('Hard', '52') == "Money doubled ---- Score : 52 ---- Difficulty : Hard"

    def test_error(self):
        assert routes.result('Extra Hard', '10') == "Error, please try again"