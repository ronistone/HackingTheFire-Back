from app import app,mongo, api
from flask_restful import Resource, reqparse
from flask import request
from bson.objectid import ObjectId


class RecursoAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("long", type=str, required=True, location='form')
        self.reqparse.add_argument("lat", type=str, location='form')


    def get(self):
        try:
            _long = request.args.get("long")
            _lat  = request.args.get("lat")
            _raio = request.args.get("raio")

            result = []
            recurso = mongo.db.recurso

            if _long and _lat and _raio:
                pass
            else:
                result.append(recurso.find())
            return result, 200
        except Exception as error:
            print(error)
            return 500

    def post(self):
        try:
            args = self.reqparse.parse_args()
            #args = {}
            #args['long'] = request.POST["long"]
            #args['lat'] = request.POST["lat"]
            recurso = mongo.db.recurso
            result = recurso.insert(args)
            return result,200
        except Exception as error:
            print(error)
            return 500


class RecursoModifyAPI(Resource):

    def get(self,_id):
        try:
            recurso = mongo.db.recurso
            result = recurso.find_one_or_404({'_id':ObjectId(_id)})
            if(result is None):
                return 404
            return result,200
        except Exception as error:
            print(error)
            return 500

    def put(self,_id):
        try:
            args = request.json
            recurso = mongo.db.recurso
            result = recurso.find_one_and_update({'_id': ObjectId(_id)}, {'$set': args})
            if(result is None):
                return 404
            return result, 200
        except Exception as error:
            print(error)
            return 500
    def delete(self,_id):
        try:
            recurso = mongo.db.recurso
            recurso.delete_one({'_id':ObjectId(_id)})
            return 200
        except Exception as error:
            print(error)
            return 500


api.add_resource(RecursoAPI,'/recurso/', endpoint='recurso')
api.add_resource(RecursoModifyAPI,'/recurso/<_id>/', endpoint='recursoModify')
