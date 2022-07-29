from flask import Blueprint, request, jsonify
from src.app.db import read, save
from src.app.utils import exist_key, exist_value
technology = Blueprint('technology', __name__, url_prefix="/technology")

@technology.route('/', methods = ["GET"])
def list_all_technologies():

  techs = read()
  return jsonify(techs), 200

@technology.route('/', methods = ["POST"])
def add_new_technology():
  list_keys = ["id", "tech"]

  data = exist_key(request.get_json(), list_keys)

  if 'error' in data:
    return jsonify(data), 400
  
  techs = read()

  if techs == None or len(techs) == 0:
    save([data])
    return jsonify(data), 201

  if exist_value(data, techs):
    return jsonify({"error": "Algum dos items que foi enviado, já existe no banco de dados"}), 400

  techs.append(data)
  save(techs)

  return jsonify(techs), 201

@technology.route('/<int:id>', methods = ["DELETE"])
def delete_technology(id):

  techs = read()

  if techs == None or len(techs) == 0:
    return {"error": f"id {id} não foi encontrado"}, 404

  for index, data in enumerate(techs):
    if data['id'] == id:
      techs.pop(index)
      save(techs)

      return jsonify({"message": f"O id {id} foi deletado com sucesso"}), 200
    
  return jsonify({"error": f"id {id} não foi encontrado"}), 404
