import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Development(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

class Production(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

app_config = {"development": Development, "production": Production}