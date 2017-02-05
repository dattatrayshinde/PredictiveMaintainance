#python "/home/lenovo/projects/PredictiveMaintainance/app.py"
#http://localhost:5000/models
from flask import Flask, render_template, request, redirect
import os
import pymongo
from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost:27017')
    db = client.PM
    return db

app = Flask(__name__)
db = get_db()

@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    return "Welcome to Predictive Maintainance Application !!!"

@app.route("/models", methods=['GET'])
def models():
    res =  db.ModelRunHistory.find()
    return render_template('/models.html', result=res)

# Remove the "debug=True" for production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    server="localhost"
    app.run(host=server, port=port, debug=True)


