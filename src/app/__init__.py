import os
from flask import Flask, jsonify
from src.app.config import app_config
from src.app.routes import routes
app = Flask(__name__)

app.config.from_object(app_config[os.getenv('FLASK_ENV')])
routes(app)

@app.route('/developers', methods = ['POST'])
def hello_world():

  return jsonify({"records": "Info"}), 400

