from app import app,mongo, api
from flask_restful import Resource, reqparse
from flask import request
from bson.json_util import dumps
from bson import json_util
import json


class ChamadaAPI(Resource):
    def get(self):
        chamada = mongo.db.chamada
        result = []
        for c in chamada.find():
            result.append(c)
        return {'result': json.dumps(result,default=json_util.default)},200

    def post(self):
        args = request.json
        chamada = mongo.db.chamada
        chamada.insert(args)
        return 200

    def put(self):
        pass

    def delete(self):
        pass

class ChamadaModifyAPI(Resource):
    def get(self,id):
        chamada = mongo.db.find(id)
        result = []
        for c in chamada.find():
            result.append(c)
        return {'result': json.dumps(result,default=json_util.default)},200


api.add_resource(ChamadaAPI,'/chamada', endpoint='chamada')
api.add_resource(ChamadaModifyAPI,'/chamada/<int:id>', endpoint='chamadaModify')


