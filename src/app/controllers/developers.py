from flask import Blueprint

developers = Blueprint('developers', __name__, url_prefix="/developer")

@developers.route('/', methods = ["GET"])
def list_all_developers():


  return {"data": ["Fulano", "Cicláno"]}