from flask import Blueprint, request

technology = Blueprint('technology', __name__, url_prefix="/technology")

@technology.route('/', methods = ["GET"])
def list_all_technologies():
  return {"data": ["Javascript", "Python", "Java"]}

@technology.route('/', methods = ["POST"])
def add_new_technology():

  data = request.get_json()

  if isinstance(data, list):
    data.append({"text": 1})
    print(data)
  return {"data": ["Javascript", "Python", "Java"]}
