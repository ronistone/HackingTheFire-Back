from app import app,mongo, api
from flask_restful import Resource
from flask import request
from bson.objectid import ObjectId


class ChamadaAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("chd_telefone", type=str, required=True, location='form')
        self.reqparse.add_argument("chd_solicitante", type=str, location='form')
        self.reqparse.add_argument("chd_municipio", type=str, location='form')
        self.reqparse.add_argument("chd_endereco", type=str, location='form')
        self.reqparse.add_argument("chd_numero", type=str, location='form')
        self.reqparse.add_argument("chd_bairro", type=str, location='form')
        self.reqparse.add_argument("chd_referencia", type=str, location='form')
        self.reqparse.add_argument("chd_paciente", type=str, location='form')
        self.reqparse.add_argument("chd_observacoes", type=str, location='form')
        self.reqparse.add_argument("chd_emergencia", type=bool, location='form')
        self.reqparse.add_argument("chd_emergencia_info", type=str, location='form')

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
            args = self.reqparse.parse_args()
            #args = request.json
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
        try:
            chamada = mongo.db.chamada
            result = chamada.find_one_and_update({'_id':ObjectId(_id)},{"$set":request.json})
            return result,200
        except Exception as error:
            print(error)
            return {"msg": "Unexpected error"},500

    def delete(self,_id):
        try:
            chamada = mongo.db.chamada
            chamada.delete_one({'_id': ObjectId(_id)})
            return 200
        except Exception as error:
            print(error)
            return {"msg": "Unexpected error"},500


api.add_resource(ChamadaAPI,'/chamada/', endpoint='chamada')
api.add_resource(ChamadaModifyAPI,'/chamada/<_id>/', endpoint='chamadaModify')


