from app import app,mongo, api
from flask_restful import Resource, reqparse
from flask import request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import json_util
import json


class ChamadaAPI(Resource):
    def get(self):
        try:
            chamada = mongo.db.chamada
            result = chamada.find()
            return result,200
        except Exception as error:
            print(error)
            return {"msg": "Unexpected error"},500

    def post(self):
        try:
            args = request.json
            chamada = mongo.db.chamada
            result = chamada.insert(args)
            return result,200
        except Exception as error:
            print(error)
            return {"msg": "Unexpected error"},500

class ChamadaModifyAPI(Resource):

    def get(self,_id):
        try:
            chamada = mongo.db.chamada
            result = chamada.find_one_or_404({"_id":ObjectId(_id)})
            return result,200
        except Exception as error:
            print(error)
            return {"msg": "Unexpected error"},500


    def put(self,_id):
        chamada = mongo.db.chamada
        result = chamada.find_one_and_update({'_id':ObjectId(_id)},{"$set":request.json})
        return result,200

    def delete(self,_id):
        chamada = mongo.db.chamada
        chamada.delete_one({'_id': ObjectId(_id)})
        return 200


api.add_resource(ChamadaAPI,'/chamada', endpoint='chamada')
api.add_resource(ChamadaModifyAPI,'/chamada/<_id>', endpoint='chamadaModify')


