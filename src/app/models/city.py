from src.app import DB, MA
from src.app.models.state import State

class City(DB.Model):
  __tablename__ = 'cities'
  id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
  state_id = DB.Column(DB.Integer, DB.ForeignKey(State.id), nullable = False)
  name = DB.Column(DB.String(84), nullable = False)

  def __init__(self, state_id, name):
    self.state_id = state_id
    self.name = name

class CitySchema(MA.Schema):
  class Meta:
    fields = ('id', 'state_id', 'name')

city_share_schema = CitySchema()
cities_share_schema = CitySchema(many = True)