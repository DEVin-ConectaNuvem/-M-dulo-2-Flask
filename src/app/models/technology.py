from flask_sqlalchemy import Model
from src.app import DB, MA

class Technology(DB.Model):
  __tablename__ = 'technologies'
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  name = DB.Column(DB.String(84), nullable=False)

  def __init__(self, name):
    self.name = name
<<<<<<< HEAD
  
=======

>>>>>>> 8ca549fe3251b6b0123b12940f044f84c0fb363b
  @classmethod
  def seed(cls, name):
    tech = Technology(
      name = name
    )
    tech.save()

<<<<<<< HEAD
  def save(self):
    DB.session.add(self)
    DB.session.commit()
=======
  def save(self): 
    DB.session.add(self)
    DB.session.commit()

>>>>>>> 8ca549fe3251b6b0123b12940f044f84c0fb363b
class TechnologySchema(MA.Schema):
  class Meta:
    fields = ('id', 'name')
    
technology_share_schema = TechnologySchema()
technologies_share_schema = TechnologySchema(many=True)