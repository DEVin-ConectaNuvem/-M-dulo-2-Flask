from src.app import DB, MA
from src.app.models.developer import Developer
from src.app.models.technology import Technology

class DeveloperTechnology(DB.Model):
  __tablename__ = 'developer_technologies'
  id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
  technology_id = DB.Column(DB.Integer, DB.ForeignKey(Technology.id), nullable = False)
  developer_id = DB.Column(DB.Integer, DB.ForeignKey(Developer.id), nullable = False)
  is_main_tech = DB.Column(DB.Boolean, nullable = False, default = False)

  def __init__(self, technology_id, developer_id, is_main_tech):
    self.technology_id = technology_id
    self.developer_id = developer_id
    self.is_main_tech = is_main_tech

class DeveloperTechnologySchema(MA.Schema):
  class Meta:
    fields = ('id', 'technology_id', 'developer_id', 'is_main_tech')

developer_technology_schema = DeveloperTechnologySchema()
developer_technologies_schema = DeveloperTechnologySchema(many = True)