"""
    Test Main module
"""
from unittest import TestCase

from fastapi import FastAPI

from app.core.main import app
from app.tests.base_test import BaseTest


class TestMain(BaseTest, TestCase):
    """
    TestMain

    Args:
        app: FastApi
    """

    app: FastAPI

    # pylint: disable=C0103
    def setUp(self):
        # pylint: enable=C0103
        """
        create default app every that TestMain trigger is started.
        """
        self.app = app

    def test_app_is_instance_of_fast_api(self):
        """
        asserts True if app is an FastAPI instance
        """
        self.assertIsInstance(self.app, FastAPI)
