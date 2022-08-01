from flask import Blueprint, request, jsonify
from src.app.db import read, save
from src.app.utils import exist_key, exist_value
technology = Blueprint('technology', __name__, url_prefix="/technology")

@technology.route('/', methods = ["GET"])
def list_all_technologies():

  techs = read('technologies')

  if techs == None or len(techs) == 0:
    return jsonify({"error": "A lista de tecnologias está vazia"}), 400
  
  return jsonify(techs), 200

@technology.route('/', methods = ["POST"])
def add_new_technology():
  list_keys = ["id", "tech"]

  data = exist_key(request.get_json(), list_keys)

  if 'error' in data:
    return jsonify(data), 400
  
  techs = read('technologies')

  if techs == None or len(techs) == 0:
    save([data], 'technologies')
    return jsonify(data), 201

  if exist_value(data, techs):
    return jsonify({"error": "Algum dos items que foi enviado, já existe no banco de dados"}), 400

  techs.append(data)
  save(techs, 'technologies')

  return jsonify(techs), 201

@technology.route('/<int:id>', methods = ["DELETE"])
def delete_technology(id):

  techs = read('technologies')
  if techs == None or len(techs) == 0:
      return {"error": "Não tem nenhuma tecnologia para deletar"}, 400
  
  for index, data in enumerate(techs):
    if data['id'] == id:
      techs.pop(index)
      save(techs, 'technologies')

      return jsonify({"message": "Item deletado com sucesso."}), 200

  return jsonify({"error": f"Não foi encontrado o id {id}"})