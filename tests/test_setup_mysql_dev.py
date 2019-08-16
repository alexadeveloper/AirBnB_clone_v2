#!/usr/bin/python3
"""test for mysql"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import MySQLdb


class TestDBase(unittest.TestCase):
    """this will test the console"""
    def test_fdb(self):
        """ test database """
        # test = os.system("./setup_mysql_dev.sql")
        pass
