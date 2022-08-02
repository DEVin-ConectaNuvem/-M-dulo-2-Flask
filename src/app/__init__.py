import os
from flask import Flask, jsonify
from src.app.config import app_config
from src.app.routes import routes
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()

def create_app():

  app = Flask(__name__)

  app.config.from_object(app_config[os.getenv('FLASK_ENV')])
  db.init_app(app)
  ma.init_app(app)
  routes(app)
  Migrate(app=app, db=db, directory='./src/app/migrations')

  return app
