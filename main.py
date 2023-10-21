from flask import Flask, render_template, request, jsonify,redirect,session,url_for
import json
import os
from pymongo import MongoClient
from flask_cors import CORS


app = Flask(__name__, static_folder='static')
uri = "mongodb+srv://dlovej009:Dheeraj2006@cluster0.dnu8vna.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['Sri_Lakshya_Project']
collection = db['Queries']
app.secret_key = 'Sri_Lakshya_Project'
CORS(app, resources={r"/submit": {"origins": "*"}})

@app.route('/submit', methods=['POST', 'OPTIONS'])
def submit_data():
    if request.method == 'OPTIONS':
        response = jsonify(message='CORS preflight request allowed')
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    elif request.method == 'POST':
        # Handle POST request as usual
        data = request.get_json()  # Get JSON data from the request
        collection.insert_one(data)
        print("done")
        return jsonify(message='Data inserted successfully'), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=11000)