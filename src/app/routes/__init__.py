from flask import Flask
from src.app.controllers.technologies import technology
from src.app.controllers.developers import developers
from src.app.controllers.cities import cities

def routes(app: Flask):
  app.register_blueprint(technology)
  app.register_blueprint(developers)
  app.register_blueprint(cities)