from src.app import DB, MA
from src.app.models.user import User

class Developer(DB.Model):
  __tablename__ = "developers"
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  months_experience = DB.Column(DB.Integer, nullable = False)
  accepted_remote_work = DB.Column(DB.Boolean, nullable = False, default = True)
  user_id = DB.Column(DB.Integer, DB.ForeignKey(User.id), nullable = True)

  def __init__(self, months_experience, accepted_remote_work, user_id):
    self.months_experience = months_experience
    self.accepted_remote_work = accepted_remote_work
    self.user_id = user_id

class DeveloperSchema(MA.Schema):
  class Meta:
    fields = ('id', 'months_experience', 'accepted_remote_work', 'user_id')

developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many = True)

