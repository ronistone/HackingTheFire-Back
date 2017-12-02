from flask import Flask
from flask_script import Manager
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')



manager = Manager(app)
mongo = PyMongo(app)
api = Api(app)

@app.route("/")
def home():
    return "OKOKOK"

from app.controllers import chamada