import pytest, unittest
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

class TestApp(TestBase):
    def test_home_page(self):
        response = self.client.get(url_for('result'))
        self.assertEqual(response.status_code, 200)