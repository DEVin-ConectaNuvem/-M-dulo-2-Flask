from src.app import DB, MA
from src.app.models.city import City

class User(DB.Model):
  __tablename__ = 'users'
  id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
  city_id = DB.Column(DB.Integer, DB.ForeignKey(City.id), nullable = False)
  name = DB.Column(DB.String(84), nullable = False)
  age = DB.Column(DB.Integer, nullable = False)
  email = DB.Column(DB.String(84), nullable = False)
  password = DB.Column(DB.String(84), nullable = False)

  def __init__(self, city_id, name, age, email, password):
    self.city_id = city_id
    self.name = name
    self.age = age
    self.email = email
    self.password = password

class UserSchema(MA.Schema):
  class Meta: 
    fields = ('id', 'city_id', 'name', 'age', 'email', 'password')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many = True)