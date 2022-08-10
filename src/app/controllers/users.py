from flask import Blueprint, request, jsonify
from src.app.middlewares.auth import jwt_required, requires_access_level
from src.app.utils import exist_key
from src.app.services.users_service import create_user, login_user

user = Blueprint('user', __name__, url_prefix="/user")

@user.route('/create', methods = ["POST"])
@requires_access_level("WRITE")
def create():
  list_keys = ["city_id", "name", "age", "email", "password"]

  data = exist_key(request.get_json(), list_keys)

  roles = None

  if "roles" in data:
    roles = data['roles']
  
  response = create_user(
    data["city_id"],
    data["name"],
    data["age"], 
    data["email"], 
    data["password"],
    roles
  )

  if "error" in response:
    return jsonify(response), 400

  return jsonify(response), 201
  
@user.route('/login', methods = ["POST"])
def login():
  list_keys = ["email", "password"]

  data = exist_key(request.get_json(), list_keys)

  response = login_user(data["email"], data["password"])

  if "error" in response:
    return jsonify({"error": response['error']}), response['status_code']

  return jsonify(response), 200