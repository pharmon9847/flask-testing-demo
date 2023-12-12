"""Sample test suite for testing demo"""

from unittest import TestCase
from app import app
from flask import session

# make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# this is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ColorViewsTestCase(TestCase):
    """Examples of integration tests: testing Flask app."""
    
    