import csv
import json
import requests
import dns
import time
from pymongo import MongoClient
from flask import Flask, render_template, url_for
from bson import BSON
from bson import json_util 

app = Flask(__name__)

client = MongoClient('mongodb+srv://isaicv18:kb0GMCojP5kW8SIX@cluster0-iroqa.azure.mongodb.net/test?retryWrites=true&w=majority')

db = client.test

r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=6167865&APPID=b398b6a3a8b44ed50d59162aeea27792")
if r.status_code == 200:
    data = r.json()
    #print("****************************************************")
    #print(data)
    db.weather.insert_one(data)
    #time.sleep(600)
else:
    exit()


collection = db['weather']
cursor = collection.find({})
for document in cursor:
    final = json.dumps(document, indent=4, default=json_util.default)


x=requests.get('http://api.openweathermap.org/data/2.5/forecast?id=6167865&APPID=b398b6a3a8b44ed50d59162aeea27792')
x=x.json()
dic=x["list"]
f = csv.writer(open("test.csv", "w+"))

for dic1 in dic:
    #print(dic1)
    tk=dic1["main"]["temp"]
    tc=int(tk)-273.15
    dic1["main"]["temp"]=str(round(tc,2))

    tk=dic1["main"]["temp_min"]
    tc=int(tk)-273.15
    dic1["main"]["temp_min"]=str(round(tc,2))

    tk=dic1["main"]["temp_max"]
    tc=int(tk)-273.15
    dic1["main"]["temp_max"]=str(round(tc,2))

    f.writerow([dic1["dt_txt"],
                dic1["main"]["temp"],
                dic1["main"]["temp_min"],
                dic1["main"]["temp_max"],
                dic1["main"]["pressure"],
                dic1["main"]["sea_level"],
                dic1["main"]["grnd_level"],
                dic1["main"]["humidity"],
                dic1["main"]["temp_kf"]])


f = open( 'test.csv', 'rU' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "Date","temp","temp_min","temp_max","pressure","sea_level","grnd_level","humidity","temp_kf" ))  
# Parse the CSV into JSON  
a = json.dumps( [ row for row in reader ] )
posts2=a.replace('"', "'")

posts = json.loads(a)  


print(posts)




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)