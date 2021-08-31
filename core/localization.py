import json

def language(id):
  with open("./data/guildinfo.json",mode="r",encoding="utf-8") as file:
    gdif=json.load(file)

  for x in gdif:
    if x == str(id):
      lan=gdif[x]["lan"]
      return lan
  return "zhtw"

  
