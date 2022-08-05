from src.app.models.developer import Developer, developers_share_schema
from src.app.models.technology import technologies_share_schema

def list_all_developers_service():

  list_developers = Developer.query.all()
  list_developers_dict = developers_share_schema.dump(list_developers)
  
  list_all_developers = []
  for developers in list_developers_dict:
    technology_dict = technologies_share_schema.dump(developers['technologies'])
    list_all_developers.append(
      {
        "technologies": technology_dict, 
        'id': developers['id'],
        'months_experience': developers['months_experience'],
        'accepted_remote_work': developers['accepted_remote_work']
      }
    )

  return list_all_developers