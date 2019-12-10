import requests
import dns
import time
from pymongo import MongoClient
import json
from bson import BSON
from bson import json_util 

client = MongoClient('mongodb+srv://isaicv18:kb0GMCojP5kW8SIX@cluster0-iroqa.azure.mongodb.net/test?retryWrites=true&w=majority')

db = client.test
while True:
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=6167865&APPID=b398b6a3a8b44ed50d59162aeea27792")
    if r.status_code == 200:
        data = r.json()
        print(data)
        db.weather.insert_one(data)
        time.sleep(600)
else:
    exit()

collection = db['weather']
cursor = collection.find({})
for document in cursor:
    final = json.dumps(document, indent=4, default=json_util.default)
print(final)
exit()