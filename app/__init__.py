from flask import Flask, make_response, send_from_directory
from flask_script import Manager
from flask_pymongo import PyMongo
from flask_restful import Api
from bson.json_util import dumps

app = Flask(__name__)
app.config.from_object('config')



manager = Manager(app)
mongo = PyMongo(app)
api = Api(app)

def output_json(obj, code, headers=None):
    """
    This is needed because we need to use a custom JSON converter
    that knows how to translate MongoDB types to JSON.
    """
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})

    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api.representations = DEFAULT_REPRESENTATIONS

@app.route("/")
def home():
    return send_from_directory("../docs/", "request.txt")


from app.controllers import chamada