import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Development(object):
  DEBUG = True
  TESTING = False

class Production(object):
  DEBUG = False
  TESTING = False

app_config = {"development": Development, "production": Production}