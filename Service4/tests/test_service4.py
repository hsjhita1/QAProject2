import pytest, unittest, requests, flask
import requests_mock
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
    def test_view(self):
        response = self.client.get(url_for('result'))
        self.assertEqual(response.status_code, 200)


def test_result(requests_mock):
    requests_mock.get('http://service2:8001', text='38')
    requests_mock.get('http://service3:8002', text='Easy')
    requests_mock.get('http://service4:8003')
    difficulty = requests.get('http://service3:8002').text
    total = requests.get('http://service2:8001').text

    response = requests_mock.post(
        url_for('result'),
        data = dict(
            difficulty = difficulty,
            total = total
        ),
            follow_redirects = True
    )
    assert ("Money back ---- Score : " + total + " ----  Difficulty : " + difficulty) == response.data
