import pytest, unittest
from application import app, routes
from flask import url_for
from flask_testing import TestCase
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'test'
        return app

class TestApp(TestBase):
    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)