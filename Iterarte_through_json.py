
import json


f = open('personal.json', "r", encoding="utf-8")
data = json.load(f)
f.close()
(print(data["results"]))