from flask import json

def save(data, db_name): 
    json_object = json.dumps(data, indent=4)
    with open(f'src/app/db/{db_name}.json', 'w') as outFile:
      outFile.write(json_object)

def read(db_name):
  try:
    with open(f'src/app/db/{db_name}.json', 'r') as openFile:
      json_object = json.load(openFile)
      return json_object

  except:
    return None