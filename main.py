from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#@app.route('/temperature', methods=['POST'])
#def temperature():
#zipcode = request.form['zip']
r = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=b398b6a3a8b44ed50d59162aeea27792')
print(r)    

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)