from flask import json

def save(data): 
    json_object = json.dumps(data, indent=4)
    with open('src/app/db/technologies.json', 'w') as outFile:
      outFile.write(json_object)

def read():
  try:
    with open('src/app/db/technologies.json', 'r') as openFile:
      json_object = json.load(openFile)
      return json_object

  except:
    return None